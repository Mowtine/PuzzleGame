# Main menu is basically like a Board class - copy Board.py It needs a variable which is a list of buttons. 
#The buttons will be added manually. It will need a GetButton, Click and Display

from Button import Button
     
     
class MainMenu():
    
    def __init__(self, x, y, w, h):
        
        self.ButtonsList = []
        self.ButtonWidth = 50
        self.ButtonHeight = 50
        
        self.Button1 = Button(x, y, self.ButtonHeight, self.ButtonWidth)
        self.Button2 = Button(x + x/4, y, self.ButtonHeight, self.ButtonWidth)
        self.Button3 = Button(x - x/4, y, self.ButtonHeight, self.ButtonWidth)
        
        self.ButtonsList.append(self.Button1)
        self.ButtonsList.append(self.Button2)
        self.ButtonsList.append(self.Button3)
        
    def Display(self):
        for Button in self.ButtonsList:
            Button.Display()
                
    def GetButton(self, x, y):
        for Button in self.ButtonsList:
            if Button.IsIn(x, y):
                return Button
        return None
    
