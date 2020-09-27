import time
import json
from .models import GameBoard

class Move:
    def __init__(self, user=None, column = None, token = None):
        '''
        Data Structure to define Move related information

        Keyword arguments:
        user: "Y"/ "R",
        column: Column no. in which coin dropped(1 based indexing),
        token: Session token
        '''
        self.user = user
        self.column = column
        self.token = token


def set_moves(move,data):
    dc = [
            data.move_num,
             {
                 "user": move.user,
                 "Column": move.column
            }
        ]
    fetch_moves = json.loads(data.all_moves or "[]")
    fetch_moves.extend(dc)
    data.all_moves = fetch_moves
    data.save()
    return True


def get_moves(data):
    return data.all_moves


def valid_token(move, db_obj):
    '''
    Checks if token is valid or not
    Returns Boolen result, Reason/Data
    '''

    result = None
    if GameBoard.objects.filter(token=move.token).exists():
        data = GameBoard.objects.get(token=move.token)
        if (time.time() - data.datetime.timestamp())//60 > 30:
            result = [False, 'INVALID, Session expired']
        else:
            result = [True, data]
    else:
        result = [False, 'INVALID, Invalid Token']
    return result

def valid_move(move,data):
    if (data.move_num%2 == 0 and move.user != 'Y')  or (data.move_num%2 != 0 and move.user != 'R'):
        print(data.move_num%2,move.user)
        return 'INVALID'
    
    rows = [
            data.row1,
            data.row2,
            data.row3,
            data.row4,
            data.row5,
            data.row6,
            ]
    
    matrix = [list(str(r)) for i in rows]

    for i in range(6):
        if matrix[i][move.column] !=0:
            if i-1<0:
                return 'INVALID'
            else:
                if move.user=='Y':
                    matrix[i-1][move.column] = 1
                else:
                    matrix[i-1][move.column] = 2
    else:
        return 'INVALID'

    set_moves(move, data)
    return 'VALID'

    


def make_move(move, db_obj):
    '''
    Returns 'VALID/INVALID' move along with 'USER WIN'

    Keywords argument:
    user: "Red" or "Yellow"
    column: "Column number choosen by user"
    '''

    response = valid_token(move, db_obj)
    if response[0]:
        data = response[1]
        return valid_move(move, data)
    else:
        return response
    