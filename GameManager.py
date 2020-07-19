from Board import Board 
from MoveCounter import MoveCounter 

class GameManager():
    
    def __init__(self, ):
        self.playerBoard = Board()
        self.refBoard = Board()
        self.MoveCounter = MoveCounter()
        
    def MouseClick(self, squareX, squareY):
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
        
    def Display(self):
        self.playerBoard.Display()
        self.refBoard.Display()
        self.MoveCounter.Display()
        
