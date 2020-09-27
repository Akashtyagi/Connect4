from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import GameBoard
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import game_activity


GameBoard_obj = GameBoard()


@api_view(['GET'])
def start(request):
    db_obj = GameBoard()
    db_obj.save()
    json = {"Response": "Ready",
            "Token": db_obj.token}
    return Response(json)


@api_view(['GET'])
def move(request):
    user = request.GET.get('u', '')
    column = request.GET.get('c', '')
    token = request.GET.get('t','')
    move = game_activity.Move(user= user,
                              column= column,
                              token= token)
    move_result = game_activity.make_move(move,GameBoard_obj)
    return Response(move_result)

@api_view(['GET'])
def all_moves(request):
    token = request.GET.get('t','')
    move = game_activity.Move(token= token)
    result = game_activity.valid_token(move,GameBoard_obj)
    if result[0]:
        return Response(game_activity.get_moves(result[1]))
    else:
        return Response(result[1])
