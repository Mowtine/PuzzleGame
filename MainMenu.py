# Main menu is basically like a Board class - copy Board.py It needs a variable which is a list of buttons. 
#The buttons will be added manually. It will need a GetButton, Click and Display

from Button import Button
     
     
class Mainmenu():
    
    def __init__(self, x, y):
        
        self.ButtonsList = []
        self.ButtonWidth = 50
        self.ButtonHeight = 50
        
        self.Button1Centre = screenWidth/2, screenHeight/2
        self.Button2Centre = screenWidth/2 + screenWidth/4, screenHeight/2
        self.Button3Centre = screenWidth/2 - screenWidth/4, screenHeight/2
        
        self.Button1 = Button(screenWidth/2, screenHeight/2, ButtonHeight, ButtonWidth, 20)
        self.Button2 = Button(screenWidth/2 + screenWidth/4, screenHeight/2, ButtonHeight, ButtonWidth, 20)
        self.Button3 = Button(screenWidth/2 - screenWidth/4, screenHeight/2, ButtonHeight, ButtonWidth, 20)
        
        self.ButtonsList.append(Button1Centre)
        self.ButtonsList.append(Button2Centre)
        self.ButtonsList.append(Button3Centre)
         
    
     
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
        
        for Button in self.ButtonsList:
        if x < Button + ButtonWidth/2, x > Button - ButtonWidth/2, y > Button - ButtonHeight/2, y < Button + ButtonHeight/2
        return Button
    
        elif
        continue
    
