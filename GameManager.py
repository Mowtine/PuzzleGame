from Board import Board 
from MoveCounter import MoveCounter
from LevelGenerator import LevelGenerator
from Timer import Timer
from MainMenu import MainMenu
from LevelSelect import LevelSelect
from LevelComplete import LevelComplete

class GameManager():
    
    def __init__(self, screenWidth, screenHeight, board1X, board1Y, board1Z, board2X, board2Y, board2Z, countersX, countersY, countersZ, timerX, timerY, timerZ):
        
        self.currentScene = "menu"
        
        self.playerBoard = Board(board1X, board1Y, board1Z)
        self.refBoard = Board(board2X, board2Y, board2Z)
        self.MoveCounter = MoveCounter(countersX, countersY, countersZ)
        self.Timer = Timer(timerX, timerY, timerZ)
        # TODO: After updating the MoveCounter, add a second counter for the MAX moves (or target moves)
        self.LevelGenerator = LevelGenerator(board2X, board2Y, board2Z)
        
        self.mainMenu = MainMenu(screenWidth/2, screenHeight/2, 50, 50)
        self.levelSelectMenu = LevelSelect(screenWidth/2, screenHeight/2, 50, 50)
        self.levelCompleteMenu = LevelComplete(screenWidth/2, screenHeight/2, 50, 50)

                
        self.resetList =[self.playerBoard, self.refBoard, self.MoveCounter, self.Timer, self.LevelGenerator]
        
        
        
        
    def Click(self, x, y):
        if self.currentScene == "level":
            squareX, squareY = self.playerBoard.GetSquare(x, y)
            if squareX != -1:
                self.playerBoard.Click(squareX, squareY)
                self.MoveCounter.Add()
                
                if self.CheckWin():
                    self.ChangeScene("level complete")
                
        elif self.currentScene == "menu":
            button = self.mainMenu.GetButton(x, y)
            if button is not None:
                self.ChangeScene(button.Value)
        
        elif self.currentScene == "select menu":
            button = self.levelSelectMenu.GetButton(x, y)
            if button is not None:
                self.ChangeScene(button.Value)
            
        elif self.currentScene == "level complete":
            button = self.levelCompleteMenu.GetButton(x, y)
            if button is not None:
                self.ChangeScene(button.Value)
            
        elif self.currentScene == "settings":
            pass
            
            
        else:
            self.currentScene = "menu"
            
    def ChangeScene(self, newScene):
        if "complete" not in newScene:
            for object in self.resetList:
                object.Reset()
        else:
            self.Timer.Pause()
        if "level" in newScene:
            pass
        
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
            
        elif self.currentScene == "select menu":
            self.levelSelectMenu.Display()
            
        elif self.currentScene == "level complete":
            self.playerBoard.Display()
            self.refBoard.Display()
            self.MoveCounter.Display()
            self.Timer.Display()
            # Task 3: Gray out what is behind it Look at processing docs, 
            self.levelCompleteMenu.Display()
        
        
        elif self.currentScene == "settings":
            pass
            
            
        else:
            self.currentScene = "menu"
        
        
