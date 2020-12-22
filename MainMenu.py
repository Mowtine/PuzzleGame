# Main menu is basically like a Board class - copy Board.py It needs a variable which is a list of buttons. 
#The buttons will be added manually. It will need a GetButton, Click and Display

from Button import Button
     
     
class MainMenu():
    
    def __init__(self, x, y, w, h):
        
        self.ButtonsList = []
        self.ButtonWidth = 300
        self.ButtonHeight = 200
        
        # TASK 1: Change these variables:
        self.Button1 = Button(x, y - y/2.1, self.ButtonHeight, self.ButtonWidth, "Arcade", "level", 40) 
        self.Button2 = Button(x, y + y/10, self.ButtonHeight, self.ButtonWidth, "Level select", "select menu", 40)
        self.Button3 = Button(x, y + y/1.48, self.ButtonHeight, self.ButtonWidth, "Settings", "settings", 40)
        
        self.ButtonsList.append(self.Button1)
        self.ButtonsList.append(self.Button2)
        self.ButtonsList.append(self.Button3)
        
    def Display(self):
        for Button in self.ButtonsList:
            Button.Display()
        
        fill(255)
        text('Main Menu', 250, 50)

                
    def GetButton(self, x, y):
        for Button in self.ButtonsList:
            if Button.IsIn(x, y):
                return Button
        return None
    

    


    
