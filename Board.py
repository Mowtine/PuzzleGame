from Square import Square 

class Board():
    
    def __init__(self):
        self.board = []
        for range(4):
            row = []
            for range(4):
                row.append(Square())
            self.board.append(row)
        
    def Click(self, square):
        pass
        
    def Display(self):
        pass
        
    def Reset(self):
        pass
