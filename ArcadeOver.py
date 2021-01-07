from Button import Button
     
     
class ArcadeOver():
    
    def __init__(self, x, y, w, h):
       
        

        self.ButtonsList = []
        self.ButtonWidth = 200
        self.ButtonHeight = 100
        
        # TASK 3: Make a "Next" (dw about for now) and "main menu" button. 
        self.Button1 = Button(x - x/2, y, self.ButtonHeight, self.ButtonWidth, "Restart", "1 level", 34)
        self.Button2 = Button(x + x/2, y, self.ButtonHeight, self.ButtonWidth, "Main Menu", "menu", 34)

        
        self.ButtonsList.append(self.Button1)
        self.ButtonsList.append(self.Button2)

        
    def Display(self):
        fill(0,0,0,200);
        rect(600,20,1200,3000) 
    
        for Button in self.ButtonsList:
            Button.Display()
                
    def GetButton(self, x, y):
        for Button in self.ButtonsList:
            if Button.IsIn(x, y):
                return Button
        return None
