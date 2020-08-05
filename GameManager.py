from Board import Board 
from MoveCounter import MoveCounter
from LevelGenerator import LevelGenerator
from Timer import Timer
from MainMenu import MainMenu

class GameManager():
    
    def __init__(self, screenWidth, screenHeight, board1X, board1Y, board1Z, board2X, board2Y, board2Z, countersX, countersY, countersZ, timerX, timerY, timerZ):
        
        self.currentScene = "level"
        
        self.playerBoard = Board(board1X, board1Y, board1Z)
        self.refBoard = Board(board2X, board2Y, board2Z)
        self.MoveCounter = MoveCounter(countersX, countersY, countersZ)
        self.Timer = Timer(timerX, timerY, timerZ)
        # TODO: After updating the MoveCounter, add a second counter for the MAX moves (or target moves)
        self.LevelGenerator = LevelGenerator(board2X, board2Y, board2Z)
        
        self.mainMenu = MainMenu(screenWidth/2, screenHeight/2, 50, 50)
        
        
    def Click(self, x, y):
        if self.currentScene == "level":
            squareX, squareY = self.playerBoard.GetSquare(x, y)
            if squareX != -1:
                self.playerBoard.Click(squareX, squareY)
                self.MoveCounter.Add()
                
        elif self.currentScene == "menu":
            pass
            
            
        elif self.currentScene == "settings":
            pass
            
            
        else:
            self.currentScene = "menu"
            
    def ChangeScene(self, newScene):
        # Add extra functionality
        self.currentScene = newScene
        
    def CheckWin(self):
        if self.playerBoard.Equals(self.refBoard): #Impliment Equals check in board
            return True
        else:
            return False 
        
    def Reset(self):
        self.MoveCounter.Reset()
        self.playerBoard.Reset()
        self.Timer.Reset()
        
    def GenerateLevel(self, moves):
        self.Reset()
        self.refBoard = self.LevelGenerator.GenerateLevel(moves)
        
    def Display(self):
        if self.currentScene == "level":
            self.playerBoard.Display()
            self.refBoard.Display()
            self.MoveCounter.Display()
            self.Timer.Display()
                
        elif self.currentScene == "menu":
            self.mainMenu.Display()
            
            
        elif self.currentScene == "settings":
            pass
            
            
        else:
            self.currentScene = "menu"
        
        
