from django.shortcuts import render
from django.http import HttpResponse

from . import scrabble

# Create your views here.
def index(request):
    return HttpResponse("scrabb thrabb")

def board(request):
    board = scrabble.Board()
    return HttpResponse(board.get_board())
