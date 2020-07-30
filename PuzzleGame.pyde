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

board1X = 180
board1Y = 175
board1Z = 400
board2X = 713
board2Y = 175
board2Z = 400
gameManager = GameManager(screenWidth, screenHeight, board1X, board1Y, board1Z, board2X, board2Y, board2Z)

def setup():
    
    global gameManager
    global screenWidth
    global screenHeight
    
    
    size(screenWidth, screenHeight)
    noStroke()
    fill(255)
    rectMode(CORNER)
    
    gameManager.GenerateLevel(3)


def draw():
    
    global gameManager
    
    background(255)
    
    gameManager.Display()

def mouseClicked():
    if mouseButton == LEFT:
        gameManager.Click(mouseX, mouseY)
    return
