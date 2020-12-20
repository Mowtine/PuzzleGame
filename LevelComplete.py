from Button import Button
     
     
class LevelComplete():
    
    def __init__(self, x, y, w, h):
        
        self.ButtonsList = []
        self.ButtonWidth = 50
        self.ButtonHeight = 50
        
        # TASK 3: Make a "Next" (dw about for now) and "main menu" button. 
        self.Button1 = Button(x, y, self.ButtonHeight, self.ButtonWidth, "1.0 level", "1", 34)
        self.Button2 = Button(x + x/4, y, self.ButtonHeight, self.ButtonWidth, "menu", "2.1", 34)
        self.Button3 = Button(x - x/4, y, self.ButtonHeight, self.ButtonWidth, "2.2 level", "2.2", 34)
        # Add buttons
        
        self.ButtonsList.append(self.Button1)
        self.ButtonsList.append(self.Button2)
        self.ButtonsList.append(self.Button3)
        # Add them to the list
        
    def Display(self):
        for Button in self.ButtonsList:
            Button.Display()
                
    def GetButton(self, x, y):
        for Button in self.ButtonsList:
            if Button.IsIn(x, y):
                return Button
        return None
    
