from Board import Board 
from MoveCounter import MoveCounter
from LevelGenerator import LevelGenerator
from Timer import Timer
from MainMenu import MainMenu
from LevelSelect import LevelSelect
from LevelComplete import LevelComplete
from Button import Button
from ArcadeOver import ArcadeOver


class GameManager():
    
    def __init__(self, screenWidth, screenHeight, board1X, board1Y, board1Z, board2X, board2Y, board2Z, countersX, countersY, countersZ, timerX, timerY, timerZ, arcadeLevels, gameLevels):
        
        self.currentScene = "menu"
        self.arcadeLevels = arcadeLevels
        self.currentLevel = 0
        self.gameLevels = gameLevels
        
    
        
        self.BackButton = Button(430, 40, 50, 110, "Back", "menu", 30)
        self.playerBoard = Board(board1X, board1Y, board1Z)
        self.refBoard = Board(board2X, board2Y, board2Z)
        self.MoveCounter = MoveCounter(countersX, countersY, countersZ)
        self.Timer = Timer(timerX, timerY, timerZ)
        # TODO: After updating the MoveCounter, add a second counter for the MAX moves (or target moves)
        self.LevelGenerator = LevelGenerator(board2X, board2Y, board2Z)
        
        self.mainMenu = MainMenu(screenWidth/2, screenHeight/2, 50, 50)
        self.levelSelectMenu = LevelSelect(screenWidth/2, screenHeight/2, 50, 50, self.gameLevels)
        self.levelCompleteMenu = LevelComplete(screenWidth/2, screenHeight/2, 50, 50)    
        self.arcadeOverMenu = ArcadeOver(screenWidth/2, screenHeight/2, 50, 50)
        
        self.resetList =[self.playerBoard, self.refBoard, self.MoveCounter, self.LevelGenerator]

        
        
        
        
    def Click(self, x, y):
        if "level" in self.currentScene:
            
            clicked = self.BackButton.IsIn(x, y)
            if clicked:
                self.ChangeScene(self.BackButton.Value)
                return
            
            squareX, squareY = self.playerBoard.GetSquare(x, y)
            
            if squareX != -1:
                self.playerBoard.Click(squareX, squareY)
                self.MoveCounter.Add()
                
                if self.CheckWin():
                                        
                    if "arcade" in self.currentScene:
                        self.currentLevel += 1
                        self.ChangeScene("level arcade")
                    else:
                        self.ChangeScene("complete")
                        
        elif self.currentScene == "menu":
            button = self.mainMenu.GetButton(x, y)
            if button is not None:
                self.ChangeScene(button.Value)
        
        elif self.currentScene == "select menu":
            button = self.levelSelectMenu.GetButton(x, y)
            if button is not None:
                self.ChangeScene(button.Value)
            
        elif self.currentScene == "complete":
            button = self.levelCompleteMenu.GetButton(x, y)
            if button is not None:
                if button.Value == "next level":
                    self.currentLevel +=1
                    self.ChangeScene(str(self.arcadeLevels[self.currentLevel])+" level")
            
                else:       
                    self.ChangeScene(button.Value)
        
        elif self.currentScene == "arcade complete":
            button = self.arcadeOverMenu.GetButton(x, y)
            if button is not None:
                self.currentLevel = 0
                self.ChangeScene(button.Value)
                
    
                    
                        
        #I need to add a value to the button which makes it go to next level 
        # IF we clicked on "next level" then:
        #     Check what the current level is (self.currentLevel), and increase it by 1. 
        #     Change level to that -> self.ChangeScene("2.2 level")
        elif self.currentScene == "settings":
            pass
            
            
        else:
            self.currentScene = "menu"
            
    def ChangeScene(self, newScene):
        if "complete" not in newScene:
            for object in self.resetList:
                object.Reset()
            self.Timer.Reset(self.arcadeLevels[self.currentLevel]*5)
        else:
            self.Timer.Pause()
        if "level" in newScene:
            
            if "arcade" in newScene:
                self.GenerateLevel(int(self.arcadeLevels[self.currentLevel]))
            else:
                self.GenerateLevel(int(newScene[0]))
        self.currentScene = newScene
        
    def CheckWin(self):
        if self.playerBoard.Equals(self.refBoard): #Impliment Equals check in board
            return True
        else:
            return False 
        
    def Reset(self):
        self.MoveCounter.Reset()
        self.playerBoard.Reset()
        self.Timer.Reset(self.arcadeLevels[self.currentLevel]*5)
        
    def GenerateLevel(self, moves):
        self.Reset()
        self.refBoard = self.LevelGenerator.GenerateLevel(moves)
        
    def Display(self):
        if "level" in self.currentScene:
            self.playerBoard.Display()
            self.refBoard.Display()
            self.MoveCounter.Display()
            self.Timer.Display()
            self.BackButton.Display()
            if self.Timer.OutofTime():
                self.ChangeScene("arcade complete")
                
        elif self.currentScene == "arcade complete":
            self.playerBoard.Display()
            self.refBoard.Display()
            self.MoveCounter.Display()
            self.Timer.Display()
            self.arcadeOverMenu.Display()
                 
        elif self.currentScene == "menu":
            self.mainMenu.Display()
            
        elif self.currentScene == "select menu":
            self.levelSelectMenu.Display()
        
        elif self.currentScene == "complete":
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
        
        
