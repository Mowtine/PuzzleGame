"""
Important elements + functions:
 - Board 
     - Player’s board/final board
 = Display() -> squares.Display()
 = Click(square)

- squares
     - Black/white
 = flip()
 = Display()

- Game manager
       - Move counter
 = MousePress(position) -> Click(square) -> counter
 = CheckWin(board1, board2)

- Move Counter
 =  Display()
 = Update()
 = Add()
 = Reset()
"""

from GameManager import GameManager
from MoveCounter import MoveCounter
from Board import Board

screenWidth = 1200
screenHeight = 600

board1X = 100
board1Y = 150
board1Z = 400
board2X = 700
board2Y = 150
board2Z = 400
gameManager = GameManager(screenWidth, screenHeight, board1X, board1Y, board1Z, board2X, board2Y, board2Z)
gameManager.refBoard.Click(1, 0)
gameManager.refBoard.Click(3, 2)
gameManager.refBoard.Click(2, 3)

def setup():
    
    global gameManager
    global screenWidth
    global screenHeight
    
    
    size(screenWidth, screenHeight)
    noStroke()
    fill(255)
    #rectMode(CENTER)


def draw():
    
    global gameManager
    
    background(51)
    
    gameManager.Display()

def mouseClicked():
    if mouseButton == LEFT:
        gameManager.Click(mouseX, mouseY)
    return
