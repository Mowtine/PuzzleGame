from Board import Board
import random

class LevelGenerator():
    
    def __init__(self, board2X, board2Y, board2Z):
        self.board = Board(board2X, board2Y, board2Z)
        
    def GenerateLevel(self, moves):
        
        self.board.Reset()
        xs = []
        ys = []
        for i in range(moves):
            
            x = random.randrange(0,3)
            y = random.randrange(0,3)
            
            while x in xs or y in ys:
                x = random.randrange(0,4)
                y = random.randrange(0,4)
            
            self.board.Click(x,y)
            xs.append(x)
            ys.append(y)
        
        return self.board
        
