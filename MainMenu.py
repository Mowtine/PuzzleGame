# Main menu is basically like a Board class - copy Board.py It needs a variable which is a list of buttons. 
#The buttons will be added manually. It will need a GetButton, Click and Display

from Button import Button
     
     
class Mainmenu():
    
    def __init__(self, x, y):
        
        self.Buttons = []
        Buttons.append(Button1)
        Buttons.append(Button2)
        Buttons.append(Button3)
        
        Button1Location = screenWidth/2, screenHeight/2
        Button2Centre = screenWidth/2 + screenWidth/4
        Button3Centre = screenWidth/2 - screenWidth/4
        
        Button1 = rect(screenWidth/2, screenHeight/2, 50, 50, 20)
        Button2 = rect(screenWidth/2 + screenWidth/4, screenHeight/2, 50, 50, 20)
        Button3 = rect(screenWidth/2 - screenWidth/4, screenHeight/2, 50, 50, 20)
     
     
    def Click(self, x, y):
        self.currentScene = "menu"
        self.Display
        
    def Display(self):
        fill(0)
        self.Button1
        self.Button2
        self.Button3
                
        
    def Reset(self):
        self.Display
                
    def GetButton(self, x, y):
        
        for Button in Buttons:
        if x < Button + ButtonWidth/2, x > Button - ButtonWidth/2, y > Button - ButtonHeight/2, y < Button + ButtonHeight/2
        #run button function
    
        elif
        continue
    
