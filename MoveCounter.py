
class MoveCounter():
    
    def __init__(self, xPos, yPos, zPos):
        self.MoveValue = 0
        self.xPos = xPos+235.5
        self.yPos = yPos+210

    def Update(self, value):
        self.MoveValue = value
        
    def Add(self):
        self.MoveValue = self.MoveValue + 1
        
    def Reset(self):
        self.MoveValue = 0
        
        
    def Display(self):
        
        #move counter starts here 
        #Yellow Outline
        fill(255, 204, 0)
        rect(self.xPos+47.5,self.yPos,94,50,0,7,7,0)
    
        #Yellow side
        textAlign(CENTER)
        fill(255, 204, 0)
        rect(self.xPos-40,self.yPos,85,50,7,0,0,7)
        
        loadFont("movesfont2.vlw")
        textSize(23)
    
        fill(0)
        text("Moves:",self.xPos-38,self.yPos+8)
        
        #black side
        fill(0)
        rect(self.xPos+48,self.yPos,90,48,0,7,7,0)
        
        #movevalue number
        fill(255, 204, 0)
        textSize(32)
        text(str(self.MoveValue),self.xPos+50,self.yPos+11)
