
class MoveCounter():
    
    def __init__(self):
        self.MoveValue = 0
        # TODO: Add position values to the constructor (this function) of the MoveCounter, and have it display according to that.
        
    def Update(self, value):
        self.MoveValue = value
        
    def Add(self):
        self.MoveValue = self.MoveValue + 1
        
    def Reset(self):
        self.MoveValue = 0
        
        
    def Display(self):
        textAlign(CENTER)
        fill(255, 204, 0)
        rect(560,10,80,20)
        
        fill(0)
        textSize(12)
        text("Moves: ",600,25)
        
        fill(0)
        rect(560,30,80,50)
        
        fill(255, 204, 0)
        textSize(32)
        text(str(self.MoveValue),600,65)
        
        
        
