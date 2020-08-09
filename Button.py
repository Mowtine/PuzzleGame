# Button class! It needs Display, Click, IsIn functions, and is exactly like a square class otherwise
class Button():
    
    def __init__(self, x, y, h, w, text, value):
        self.colour = "Yellow"
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.Text = text
        self.Value = value
        
    def Display(self):
        if self.colour == "Yellow":
            fill(255, 204, 0)
        else:
            fill(0)
        
        rect(self.x, self.y, self.w, self.h, 15)
        
        textAlign(CENTER)
        fill(0)
        text(self.Text,self.x ,self.y)
        
        
    def IsIn(self, x, y):
        if x > self.x - self.w/2 and x < self.x + self.w/2 and y > self.y - self.h/2 and y < self.y + self.h/2:
            return True
        else:
            return False
        
