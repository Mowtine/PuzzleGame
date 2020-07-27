from Board import Board 
from MoveCounter import MoveCounter
from LevelGenerator import LevelGenerator

class GameManager():
    
    def __init__(self, screenWidth, screenHeight, board1X, board1Y, board1Z, board2X, board2Y, board2Z):
        self.playerBoard = Board(board1X, board1Y, board1Z)
        self.refBoard = Board(board2X, board2Y, board2Z)
        self.MoveCounter = MoveCounter()
        # TODO: After updating the MoveCounter, add a second counter for the MAX moves (or target moves)
        self.LevelGenerator = LevelGenerator(board2X, board2Y, board2Z)
        
        # TODO: Impliment menus!
        #self.CurrentLevel = 
        
        
    def Click(self, x, y):
        squareX, squareY = self.playerBoard.GetSquare(x, y)
        if squareX != -1:
            self.playerBoard.Click(squareX, squareY)
            self.MoveCounter.Add()
        
    def CheckWin(self):
        if self.playerBoard.Equals(self.refBoard): #Impliment Equals check in board
            return True
        else:
            return False 
        
    def Reset(self):
        self.MoveCounter.Reset()
        self.playerBoard.Reset()
        
    def GenerateLevel(self, moves):
        self.Reset()
        self.refBoard = self.LevelGenerator.GenerateLevel(moves)
        
    def Display(self):
        self.playerBoard.Display()
        self.refBoard.Display()
        self.MoveCounter.Display()
        
