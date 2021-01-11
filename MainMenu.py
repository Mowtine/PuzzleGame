# Main menu is basically like a Board class - copy Board.py It needs a variable which is a list of buttons. 
#The buttons will be added manually. It will need a GetButton, Click and Display

from Button import Button
     
     
class MainMenu():
    
    def __init__(self, x, y, w, h):
        
        self.ButtonsList = []
        self.ButtonWidth = 250
        self.ButtonHeight = 90
        
        # TASK 1: Change these variables:
        self.Button1 = Button(x, y - 90, self.ButtonHeight, self.ButtonWidth, "Arcade", "level arcade", 35) 
        self.Button2 = Button(x, y + 20, self.ButtonHeight, self.ButtonWidth, "Level Select", "select menu", 35)
        self.Button3 = Button(x, y + 130, self.ButtonHeight, self.ButtonWidth, "Settings", "settings", 35)
        
        self.ButtonsList.append(self.Button1)
        self.ButtonsList.append(self.Button2)
        self.ButtonsList.append(self.Button3)
        
    def Display(self):
        bg = loadImage("bg3.jpg")
        background(bg)
        
        # Background art
        fill(105)
        rect(253, 403, 400, 465, 40)
        
        fill(133, 129, 118)
        rect(250, 400, 400, 465, 40)
        
        fill(255)
        rect(250, 400, 385, 450, 30)
        
        fill(227, 227, 227)
        rect(250, 400, 370, 435, 20)
        
        fill(105)
        rect(250, 175, 307, 107, 20)    
        
        fill(0)
        rect(250, 175, 300, 100, 15)


        for Button in self.ButtonsList:
            Button.Display()
        
        fill(255)
        text('Main Menu', 250, 175)

                
    def GetButton(self, x, y):
        for Button in self.ButtonsList:
            if Button.IsIn(x, y):
                return Button
        return None
    

    


    
