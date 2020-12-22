from Button import Button
     
     
class LevelSelect():
    
    def __init__(self, x, y, w, h):
        
        self.ButtonsList = []
        self.ButtonWidth = 120
        self.ButtonHeight = 120
        
        # TASK 2: Change and add buttons for each level: Level Valunes: "1.1 level"
        
        for i in range(1,5):
            y= 20 + i*160

            for j in range(0,3):    
                self.ButtonsList.append(Button(x - (x/2+20) + (x/2+20)*j, y, self.ButtonHeight, self.ButtonWidth, str(i)+"."+str(j), str(i)+"." + str(j) + " level", 26))

        
    def Display(self):
        for Button in self.ButtonsList:
            Button.Display()
            fill(255)
            text('Select Level', 250, 50)
                
    def GetButton(self, x, y):
        for Button in self.ButtonsList:
            if Button.IsIn(x, y):
                return Button
        return None
    
