from Button import Button
     
     
class LevelSelect():
    
    def __init__(self, x, y, w, h):
        
        self.ButtonsList = []
        self.ButtonWidth = 115
        self.ButtonHeight = 115
        self.levelList = [['2.0', [1, 1], [1, 2]], ['2.1', [2, 2], [3, 3]], ['2.2', [1, 4], [2, 4]], ['2.3', [2, 2], [3, 4]], ['3.0', [1, 1], [2, 2], [4, 4]], ['3.1', [3, 1], [4, 1], [4, 2]], ['3.2', [1, 1], [2, 1], [4, 3]], ['3.3', [3, 2], [1, 2], [3, 4]], ['4.0', [2, 2], [2, 3], [3, 2], [3, 3]], ['4.1', [4, 4], [2, 2], [3, 1], [2, 4]], ['4.2', [2, 1], [3, 2], [4, 3], [1, 4]], ['4.3', [4, 1], [2, 4], [3, 3], [3, 2]]]
        
        #[0][0]
        
        for i in range(1,5):
            y= 20 + i*160

            for j in range(0,3):    
                #self.ButtonsList.append(Button(x - (x/2+20) + (x/2+20)*j, y, self.ButtonHeight, self.ButtonWidth, str(i)+"."+str(j), str(i)+"." + str(j) + " level", 26))
        
                self.ButtonsList.append(Button(x - (x/2+20) + (x/2+20)*j, y, self.ButtonHeight, self.ButtonWidth, self.levelList[3*(i-1)+j][0], self.levelList[3*(i-1)+j][0] + " level", 26))
                
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
    
