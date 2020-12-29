
class MoveCounter():
    
    def __init__(self, xPos, yPos, zPos):
        self.MoveValue = 0
        self.xPos = xPos+250
        self.yPos = yPos+200

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
        rect(self.xPos+47.5,self.yPos,74,50,0,7,7,0)
    
        #Yellow side
        textAlign(CENTER)
        fill(255, 204, 0)
        rect(self.xPos-35,self.yPos,100,50,7,0,0,7)
        
        loadFont("movesfont2.vlw")
        textSize(25)
    
        fill(0)
        text("Moves: ",self.xPos-32,self.yPos+10)
        
        #black side
        fill(0)
        rect(self.xPos+48,self.yPos,70,48,0,7,7,0)
        
        #movevalue number
        fill(255, 204, 0)
        textSize(32)
        text(str(self.MoveValue),self.xPos+50,self.yPos+11)
