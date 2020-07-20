
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
        if self.colour == "White":
            fill(255)
        else:
            fill(0)
        rect(self.x, self.y, self.h, self.w)
        
    def Reset(self):
        self.colour = "White"
        
    def IsIn(self, x, y):
        if x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h:
            return True
        else:
            return False
        
