# Button class! It needs Display, Click, IsIn functions, and is exactly like a square class otherwise
class Button():
    
    def __init__(self, x, y, h, w, vartext, value, vartextSize):
        self.colour = "Yellow"
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.Text = vartext
        self.Value = value
        self.TextSize = vartextSize
        
    def Display(self):
        
        # Outline
        fill(128, 102, 0)
        rect(self.x, self.y + 5, self.w + 7, self.h + 7, 20)
        
        # Shadow
        fill(212, 169, 0)
        rect(self.x, self.y, self.w + 7, self.h + 7, 20)
        
        if self.colour == "Yellow":
            fill(255, 204, 0)
        else:
            fill(0)
        rect(self.x, self.y, self.w, self.h, 15)
        
        fill(242, 194, 0)
        rect(self.x, self.y + self.h/4, self.w, self.h/2,0,0,15,15)

        textAlign(CENTER, CENTER)
        fill(0)
        font = loadFont("font1.vlw")
        textFont(font)
        textSize(self.TextSize)
        text(self.Text,self.x ,self.y)
        
        
    def IsIn(self, x, y):
        if x > self.x - self.w/2 and x < self.x + self.w/2 and y > self.y - self.h/2 and y < self.y + self.h/2:
            return True
        else:
            return False
        
