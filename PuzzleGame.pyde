

from GameManager import GameManager
from MoveCounter import MoveCounter
from Board import Board

screenWidth = 500
screenHeight = 800

board1X = screenWidth/2
board1Y = screenHeight - screenWidth/2
board1Z = screenWidth*9/10
board2X = screenWidth/2 -screenWidth/4 + 10
board2Y = screenHeight/4
board2Z = screenWidth*7/18
countersX = screenWidth/4
countersY = screenHeight/20
countersZ = screenHeight/8
timeX = screenWidth*3/4
timeY = screenHeight/20
timeZ = screenHeight/8
gameManager = GameManager(screenWidth, 
                          screenHeight, 
                          board1X, 
                          board1Y, 
                          board1Z, 
                          board2X, 
                          board2Y, 
                          board2Z, 
                          countersX, 
                          countersY, 
                          countersZ,
                          timeX, 
                          timeY, 
                          timeZ)

def setup():
    
    global gameManager
    global screenWidth
    global screenHeight
    
    
    size(screenWidth, screenHeight)
    noStroke()
    fill(255)
    rectMode(CENTER)
    
    gameManager.GenerateLevel(3)


def draw():
    
    global gameManager
    
    background(255)
    
    #black Background at top
    fill(0)
    rect(600,20,1200,120)
    
    gameManager.Display()

def mouseClicked():
    if mouseButton == LEFT:
        gameManager.Click(mouseX, mouseY)
    return
