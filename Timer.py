
class Timer():
    
    def __init__(self, xPos, yPos, zPos):
        self.startTime = 0
        self.xPos = xPos
        self.yPos = yPos
        
    def Reset(self):
        self.startTime = millis()
        
        
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
        textSize(24)
    
        fill(0)
        text("Time: ",self.xPos-33,self.yPos+8)
        
        #black side
        fill(0)
        rect(self.xPos+48,self.yPos,90,48,0,7,7,0)
        
        #movevalue number
        fill(255, 204, 0)
        textSize(32)
        text('%.1f' % ((millis()-self.startTime)/1000.0),self.xPos+48,self.yPos+11) # Where this came from: https://stackoverflow.com/questions/6149006/display-a-float-with-two-decimal-places-in-python