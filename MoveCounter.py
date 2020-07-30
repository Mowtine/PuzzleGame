
class MoveCounter():
    
    def __init__(self, xPos, yPos):
        self.MoveValue = 0
        self.xPos = xPos = 600
        self.yPos = yPos = 50

    def Update(self, value):
        self.MoveValue = value
        
    def Add(self):
        self.MoveValue = self.MoveValue + 1
        
    def Reset(self):
        self.MoveValue = 0
        
        
    def Display(self):
        
        #black Background 
        fill(0)
        rect(600,20,1200,150)
        
        #move counter starts here 
        
        fill(255, 204, 0)
        rect(self.xPos+47.5,self.yPos,74,50,0,7,7,0)
        

        textAlign(CENTER)
        fill(255, 204, 0)
        rectMode(CENTER)
        rect(self.xPos-35,self.yPos,100,50,7,0,0,7)
        
        loadFont("movesfont2.vlw")
        textSize(24)
    
        
        fill(0)
        text("Moves: ",self.xPos-30,self.yPos+7)
        
        fill(0)
        rectMode(CENTER)
        rect(self.xPos+48,self.yPos,70,48,0,7,7,0)
        
        fill(255, 204, 0)
        textSize(32)
        text(str(self.MoveValue),self.xPos+50,self.yPos+10)
        
        
        

    

        
        
