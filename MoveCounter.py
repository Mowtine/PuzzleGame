
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
        xPos=580;
        yPos=30;

        textAlign(CENTER)
        fill(255, 204, 0)
        rectMode(CENTER)
        rect(xPos,yPos,80,20)
        
        fill(0)
        textSize(12)
        text("Moves: ",xPos,yPos+5)
        
        fill(0)
        rectMode(CENTER)
        rect(xPos,yPos+35,80,50)
        
        fill(255, 204, 0)
        textSize(32)
        text(str(self.MoveValue),xPos,yPos+45)
        
        
        
