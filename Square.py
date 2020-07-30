
class Square():
    
    def __init__(self, x, y, h, w):
        self.colour = "Yellow"
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        
    def Flip(self):
        if self.colour == "Yellow":
            self.colour = "Black"
        else:
            self.colour = "Yellow"
        
    def Display(self):
        if self.colour == "Yellow":
            fill(255, 204, 0)
        else:
            fill(0)
        rect(self.x, self.y, self.h, self.w,15)
        
    def Reset(self):
        self.colour = "Yellow"
        
    def IsIn(self, x, y):
        if x > self.x - self.w/2 and x < self.x + self.w/2 and y > self.y - self.h/2 and y < self.y + self.h/2:
            #TODO charlie: 
            return True
        else:
            return False
        
