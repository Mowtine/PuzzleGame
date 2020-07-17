from Board import Board 
from MoveCounter import MoveCounter 

class GameManager():
    
    def __init__(self):
        self.board = []
        for range(4):
            row = []
            for range(4):
                row.append(Square())
            self.board.append(row)
        
    def MouseClick(self, square):
        pass
        
    def CheckWin(self):
        pass
        
    def Reset(self):
        pass
        
    def Display(self):
        pass
