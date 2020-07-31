from Square import Square 

class Board():
    
    def __init__(self, x, y, z):
        self.board = []
        for i in range(4):
            row = []
            for j in range(4):
                # TODO: Convert this to have the distance between the squares scale properly
                row.append(Square(x-(z*9/35)*3/2 + (z*9/35)*i, y-(z*9/35)*3/2 + (z*9/35)*j, z*8/35, z*8/35))
            self.board.append(row)
        
    def Click(self, squareX, squareY):
        for i in range(4):
            self.board[squareX][i].Flip()
            self.board[i][squareY].Flip()
        self.board[squareX][squareY].Flip()
        
    def Display(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j].Display()
                
        
    def Reset(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j].Reset()
                
    def GetSquare(self, x, y):
        for i in range(4):
            for j in range(4): 
                if self.board[i][j].IsIn(x, y):
                    return i, j
        return -1, -1

        
        
