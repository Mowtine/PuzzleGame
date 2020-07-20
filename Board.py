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
       
         if (mouseButton == LEFT):
            
            self.board[x][1].Flip()
            
            self.board[x][2].Flip()
            
            self.board[x][3].Flip()
            
            self.board[x][4].Flip()
            
            self.board[1][y].Flip()
            
            self.board[2][y].Flip()
            
            self.board[3][y].Flip()
            
            self.board[4][y].Flip()
            
            
        
    def Display(self):

    for i in range(5)  #1=<i=<4
    
        self.board[i][1].Display()
        self.board[i][2].Display()
        self.board[i][3].Display()
        self.board[i][4].Display()
        
    def Reset(self):
        
        for i in range(5)  #1=<i=<4
        self.board[i][1].colour = "White"
        self.board[i][2].colour = "White"
        self.board[i][3].colour = "White"
        self.board[i][4].colour = "White"
