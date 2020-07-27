
class MoveCounter():
    
    def __init__(self, xPos, yPos):
        self.MoveValue = 0
        self.xPos = xPos
        self.yPos = yPos

    def Update(self, value):
        self.MoveValue = value
        
    def Add(self):
        self.MoveValue = self.MoveValue + 1
        
    def Reset(self):
        self.MoveValue = 0
        
        
    def Display(self):

        textAlign(CENTER)
        fill(255, 204, 0)
        rectMode(CENTER)
        rect(self.xPos,self.yPos,80,20)
        
        fill(0)
        textSize(12)
        text("Moves: ",self.xPos,self.yPos+5)
        
        fill(0)
        rectMode(CENTER)
        rect(self.xPos,self.yPos+35,80,50)
        
        fill(255, 204, 0)
        textSize(32)
        text(str(self.MoveValue),self.xPos,self.yPos+45)
        
        
        
