"""
Important elements + functions:
 - Board 
     - Player’s board/final board
 = Display() -> squares.Display()
 = Click(square)

- squares
     - Black/white
 = flip()
 = Display()

- Game manager
       - Move counter
 = MousePress(position) -> Click(square) -> counter
 = CheckWin(board1, board2)

- Move Counter
 =  Display()
 = Update()
 = Add()
 = Reset()
"""

from GameManager import GameManager
from MoveCounter import MoveCounter

def setup():
    size(640, 420)
    noStroke()
    fill(255)
    rectMode(CENTER)


def draw():
    
    background(51)

    global jitter
    # during even-numbered seconds (0, 2, 4, 6...)
    if second() % 2 == 0:
        jitter = random(-0.1, 0.1)

    global angle
    angle = angle + jitter
    c = cos(angle)
    translate(width / 2, height / 2)
    rotate(c)
    rect(0, 0, 180, 180)
