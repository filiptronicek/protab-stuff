import maze
import random

moves = ["w", "a", "s", "d"]

def canMove(x,y,field):
    return field[y][x] == 0 or field[y][x] == 3

c = maze.Connect('admin', 'tojedalka')


c.wait()
for i in range(300):
    moje_x = c.x()
    moje_y = c.y()
    if not c.move("d"):
        if not c.move("s"):
            if not c.move("a"):
                c.move("w")
while True:
    i = input("?")
    c.move(i)