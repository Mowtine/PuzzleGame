# Main menu is basically like a Board class - copy Board.py It needs a variable which is a list of buttons. The buttons will be added manually. It will need a GetButton, Click and Display
from Button import Button

#what is z point 
def __init__(self, x, y, z): 
    self.menueButtons = ["Sound","Settings"]
    for i in self.menueButtons:
            #run Button  
            for j in range(2):
                #positioning?:
                row.append(Button(x-(z*9/35)*3/2 + (z*9/35)*i, y-(z*9/35)*3/2 + (z*9/35)*j, z*8/35, z*8/35))
            self.board.append(row)

 
