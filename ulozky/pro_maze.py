import maze
import random


c = maze.Connect('admin', 'vylet')


field = c.get_all()

moje_x = c.x()
moje_y = c.y()

keyCombos = [(0, -1, "w"), (1, 0, "d"), (0, 1, "s"), (-1, 0, "a")]

positions = {
    "curr": [moje_x, moje_y]    
}

def canMove(x, y, amm):
    return (field[y][x] == 0 or field[y][x] == 3) and ([x,y] not in amm and x > 0 and y > 0)

def move(x, y, amm):
    if canMove(x,y, amm):
        positions["curr"] = [x, y]
        amm.append([x, y])
def calcPath():
    ammunation = [[positions['curr'][0], positions['curr'][1]]] # You cannot make this sound cooler
    while True:
        for moveN in keyCombos:
            if canMove(positions['curr'][0] + moveN[0], positions['curr'][1] + moveN[1], ammunation):
                move(moveN[0], moveN[1], ammunation)
                break
        if(positions['curr'] == ammunation[-1]):
            print(ammunation)
            return
        print(positions['curr'])
calcPath()