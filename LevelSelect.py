from Button import Button
     
     
class LevelSelect():
    
    def __init__(self, x, y, w, h, gameLevels):
        
        self.ButtonsList = []
        self.ButtonWidth = 115
        self.ButtonHeight = 115
        self.gameLevels = gameLevels
        #[0][0]
        
        gameLevelindex = 0 
        for i in range(1,5):
            y= 20 + i*160

            for j in range(0,3):    
                #self.ButtonsList.append(Button(x - (x/2+20) + (x/2+20)*j, y, self.ButtonHeight, self.ButtonWidth, str(i)+"."+str(j), str(i)+"." + str(j) + " level", 26))
        
                if gameLevelindex < len(gameLevels):
                    self.ButtonsList.append(Button(x - (x/2+20) + (x/2+20)*j, y, self.ButtonHeight, self.ButtonWidth, gameLevels[gameLevelindex][0], gameLevels[gameLevelindex][0] + " level", 26))    
                    gameLevelindex += 1
                
                
        self.ButtonsList.append(Button(430, 40, 50, 110, "Back", "menu", 30))  
    

        
    def Display(self):
        for Button in self.ButtonsList:
            Button.Display()
        
        fill(255)
        text('Select Level', 250, 40)    

        #fill(105)
        #rect(430, 40, 100, 100, 40)        
                        
    def GetButton(self, x, y):
        for Button in self.ButtonsList:
            if Button.IsIn(x, y):
                return Button
        return None
    
