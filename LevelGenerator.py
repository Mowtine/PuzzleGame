from Board import Board
import random

class LevelGenerator():
    
    def __init__(self, board2X, board2Y, board2Z):
        self.board = Board(board2X, board2Y, board2Z)
        self.currentMoves = 1
        
    def GenerateLevel(self, moves):
        
        self.currentMoves = moves
        
        self.board.Reset()
        xys = []
        if moves > 16:
            moves = 16
        for i in range(moves):
            
            x = random.randrange(0,3)
            y = random.randrange(0,3)
            
            while [x,y] in xys:
                x = random.randrange(0,4)
                y = random.randrange(0,4)
            
            self.board.Click(x,y)
            xys.append([x,y])
        
        
        return self.board
    

        
    def GenerateSpecificLevel(self, level): #["levelname", [2, 3]]
        
        input = ['2.0', [1, 1], [1, 2]]
        
        self.currentMoves = moves
        
        self.board.Reset()
        xys = []
        if moves > 16:
            moves = 16
                
                
        for i in range(1,len(input)):      
            x = int(input[i][0])
            y = int(input[i][1])
            

            self.board.Click(x,y)
            xys.append([x,y])
        

        return self.board
        


    def Reset(self):
        
        self.GenerateLevel(self.currentMoves)
