
class Square():
    
    def __init__(self, x, y, h, w):
        self.colour = "White"
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        
    def Flip(self):
        if self.colour == "White":
            self.colour = "Black"
        else:
            self.colour = "White"
        
        
    def Display(self):
        if self.colour == "white":
            fill(255)
        else:
            fill(0)
        rect(self.x, self.y, self.h, self.w)
        
