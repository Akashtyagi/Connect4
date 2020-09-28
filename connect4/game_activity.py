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
    dc = {
        'Move Data': {
                'user': move.user,
                'Column': move.column
                }
        }

    all_move_string = data.all_moves
    all_move_dict = json.loads(all_move_string)
    all_move_dict[str('Move '+str(data.move_num+1))] = dc
    data.all_moves = json.dumps(all_move_dict)
    return True


def get_moves(data):
    return json.loads(data.all_moves)


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
            data.delete()
        else:
            result = [True, data]
    else:
        result = [False, 'INVALID, Invalid Token']
    return result


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


def valid_move(move,data):
    if (data.move_num%2 == 0 and move.user != 'Y')  or (data.move_num%2 != 0 and move.user != 'R'):
        return 'INVALID'
    if move.column<'0' or move.column>'7':
        return 'INVALID'
    
    rows = [
            data.row1,
            data.row2,
            data.row3,
            data.row4,
            data.row5,
            data.row6,
            ]
    
    matrix = [list(str(r)) for r in rows]
    result = ''
    empty = True
    target = 0
    c = int(move.column)
    if move.user=='Y':
        target = '1'
    elif move.user=='R':
        target = '2'
    else:
        return 'INVALID'
        
    for i in range(6):
        if matrix[i][c-1] !='9':
            empty = False
            if i-1<0:
                return 'INVALID'
            matrix[i-1][c-1] = target
            print(f"Row {i-1} Col {c-1} ",matrix[i-1][c-1])
            number = int(''.join(matrix[i-1]))
            exec(f"data.row{i} = number")
            if down(i-1,c-1,target,matrix) or row(i,target,matrix):
                if target=='2':
                    result = 'RED WINS'
                else:
                    result = 'YELLOW WINS'
            else:
                result = "VALID"

    if empty:
        matrix[-1][c-1] = target
        data.row6 = int(''.join(matrix[-1]))
        if row(i,target,matrix):
            if target=='2':
                result = 'RED WINS'
            else:
                result = 'YELLOW WINS'
        else:
            result = 'VALID'

    if result:
        print("RESULt ",result)
        set_moves(move, data)
        data.move_num += 1
        data.save()
    return result


def down(row,col,target,matrix):
    count = 0
    for i in range(row,6):
        
        if matrix[i][col] == target:
            count+=1
        else:
            count=0
        if count==4:
            return True
    return count==4

def row(r,target,matrix):
    count = 0
    for i in matrix[r] :           
        if i==target:
            count+=1
        else:
            count = 0
        if count == 4:
            return True
    return count==4
