from collections import deque
import maze
import time
import random

c = maze.Connect('oof2win2', 'runda')  

def randomm():
    a = random.randint(-1000, 5000)
    b = random.randrange(-1000, 5000)
    return (a, b)

def goTo(gx, gy):
    while gx != 0  and gy != 0:
        print(c.x(), c.y())
        if gx > 0:
            c.move('w')
            gx -= 1
        elif gx < 0:
            c.move('s')
            gx += 1
        if gy > 0:
            c.move('d')
        elif gy < 0:
            c.move('a')

def randomPath():
    gx, gy = randomm()
    goTo(gx, gy)

randomPath()