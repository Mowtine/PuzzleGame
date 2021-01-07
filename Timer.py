
class Timer():
    
    def __init__(self, xPos, yPos, zPos):
        self.endTime = 0
        self.xPos = xPos-15
        self.yPos = yPos+111
        self.pause = False
        self.lastValue = 0.0
        
    def OutofTime(self):
        if self.endTime < millis():
            return True
            
    def Increment(self, extraTime):
        self.endTime = self.endTime + extraTime*1000
        self.pause = False
        
    def Reset(self, extraTime):
        self.endTime = millis() + extraTime*1000 
        self.pause = False
        
    def Pause(self):
        self.pause = True
        
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
        textSize(25)
    
        fill(0)
        text("Time:",self.xPos-37,self.yPos+8)
        
        #black side
        fill(0)
        rect(self.xPos+48,self.yPos,90,48,0,7,7,0)
        
        
        #movevalue number
        fill(255, 204, 0)
        textSize(32)
        
        if self.lastValue > 99900:
            textSize(28)
        
        if self.pause:
            self.endTime = millis() - self.lastValue
        self.lastValue = millis()-self.endTime
    
        text('%.1f' % abs(((self.endTime-millis())/1000.0)),self.xPos+48,self.yPos+11) # Where this came from: https://stackoverflow.com/questions/6149006/display-a-float-with-two-decimal-places-in-python
        

        if self.lastValue > 999900:
            self.Pause()
            
