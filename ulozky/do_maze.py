import maze
import random

moves = ["w", "a", "s", "d"]

def canMove(x,y,field):
    return field[y][x] == 0 or field[y][x] == 3

c = maze.Connect('admin', 'tojedalka')


c.wait()
while True:
    moje_x = c.x()
    moje_y = c.y()
    if canMove(moje_x, moje_y, c.get_all()): c.move(moves[1])
    if canMove(moje_x, moje_y, c.get_all()): c.move(moves[1])
