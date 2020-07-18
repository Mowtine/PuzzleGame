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
        # Change all squares in same column and row as squareX and Y
        self.board[1][2].Flip()
        
    def Display(self):
        self.board[i][j].Display()
        
    def Reset(self):
        self.board[i][j].colour = "White"
