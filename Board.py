from Square import Square 

class Board():
    
    def __init__(self):
        self.board = []
        for range(4):
            row = []
            for range(4):
                row.append(Square())
            self.board.append(row)
        
    def Click(self, squareX, squareY):
        for i in range(4):
            self.board[squareX][i].Flip()
            self.board[i][squareY].Flip()
        
    def Display(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j].Display()
        
    def Reset(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j].Reset()
                
    def GetSquare(self, x, y):
        pass
