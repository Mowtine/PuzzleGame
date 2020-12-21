from Button import Button
     
     
class LevelSelect():
    
    def __init__(self, x, y, w, h):
        
        self.ButtonsList = []
        self.ButtonWidth = 120
        self.ButtonHeight = 120
        
        # TASK 2: Change and add buttons for each level: Level Valunes: "1.1 level"
        self.Button1 = Button(x, 180, self.ButtonHeight, self.ButtonWidth, "1.1", "1.1 level", 26)
        self.Button2 = Button(x + (x/2+20), 180, self.ButtonHeight, self.ButtonWidth, "1.2", "1.2", 26)
        self.Button3 = Button(x - (x/2+20), 180, self.ButtonHeight, self.ButtonWidth, "1.0", "1", 26)
        self.Button4 = Button(x, 340, self.ButtonHeight, self.ButtonWidth, "2.1", "2.1", 26)
        self.Button5 = Button(x + (x/2+20), 340, self.ButtonHeight, self.ButtonWidth, "2.2", "2.2", 26)
        self.Button6 = Button(x - (x/2+20), 340, self.ButtonHeight, self.ButtonWidth, "2.0", "2", 26)
        self.Button7 = Button(x, 500, self.ButtonHeight, self.ButtonWidth, "3.1", "3.1", 26)
        self.Button8 = Button(x + (x/2+20), 500, self.ButtonHeight, self.ButtonWidth, "3.2", "3.2", 26)
        self.Button9 = Button(x - (x/2+20), 500, self.ButtonHeight, self.ButtonWidth, "3.0", "3", 26)
        self.Button10 = Button(x, 660, self.ButtonHeight, self.ButtonWidth, "4.1", "4.1", 26)
        self.Button11 = Button(x + (x/2+20), 660, self.ButtonHeight, self.ButtonWidth, "4.2", "4.2", 26)
        self.Button12 = Button(x - (x/2+20), 660, self.ButtonHeight, self.ButtonWidth, "4.0", "4", 26)
        # Add buttons
        
        self.ButtonsList.append(self.Button1)
        self.ButtonsList.append(self.Button2)
        self.ButtonsList.append(self.Button3)
        self.ButtonsList.append(self.Button4)
        self.ButtonsList.append(self.Button5)
        self.ButtonsList.append(self.Button6)
        self.ButtonsList.append(self.Button7)
        self.ButtonsList.append(self.Button8)
        self.ButtonsList.append(self.Button9)
        self.ButtonsList.append(self.Button10)
        self.ButtonsList.append(self.Button11)
        self.ButtonsList.append(self.Button12)
        # Add them to the list
        
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
    
