
class MoveCounter():
    
    def __init__(self):
        self.MoveValue = 0
        
    def Update(self, value):
        self.MoveValue = value
        
    def Add(self):
        self.MoveValue = self.MoveValue + 1
        
    def Reset(self):
        self.MoveValue = 0
        
        
    def Display(self):
        fill(255)
        rect(15,15,150,50)
        fill(0)
        text("Moves: " + str(self.MoveValue),40,40)
        
        
