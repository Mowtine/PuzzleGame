
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



f = open("levels.txt", "r")
arcadeString = f.readline()  
stringlevels = arcadeString.split()

arcadeLevels = [int(i) for i in stringlevels]



first = True
gameLevels = []





for initialLevels in f:
    if first: 
        first = False 
    else:
                
        
        
        initialLevelslist = initialLevels.strip().split(" ")
        clicks = []
        
        for i in range(0,len(initialLevelslist[1]),2):         
            x = int(initialLevelslist[1][i])
            y = int(initialLevelslist[1][i+1])
            
            clicks.append([x,y])
            
        
        
        gameLevels.append([initialLevelslist[0]]+clicks)
        

        


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
                          timeZ,
                          arcadeLevels,
                          gameLevels)

def setup():
    
    global gameManager
    global screenWidth
    global screenHeight
    
    
    size(screenWidth, screenHeight)
    noStroke()
    fill(255)
    rectMode(CENTER)
    
    gameManager.GenerateLevel(3)
    

            
            

         

    
    """You will have to have a loop (likely a while loop) Google how to read a file till the end in python, while there are still lines in this file.
within the while, save and process each line, like in the arcade levels
and save them to a list with the level information"""

    """gameLevels = [["levelname", [2, 3]],[ "2.1", [1,2], [3,4]]]
    ["levelname", [2, 3]]  level information
    from the file which has a line per level of:
    2.0 3423 -> ["2.0", [3,4], [2,3]]"""


    

    
    
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
