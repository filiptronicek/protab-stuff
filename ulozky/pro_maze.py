import maze
import random


c = maze.Connect('admin', 'vylet')


field = c.get_all()

moje_x = c.x()
moje_y = c.y()

keyCombos = [(0, 1, "s"), (0, -1, "w"), (1, 0, "d"), (-1, 0, "a")]

positions = {
    "curr": [moje_x, moje_y],    
}

def canMove(x, y, amm):
    return field[y][x] == 0 or field[y][x] == 3 and [x,y] not in amm

def move(x, y, amm):
    if canMove(x,y, amm):
        positions["curr"] = [x, y]
        amm.append([x, y])
def calcPath():
    ammunation = [[moje_x, moje_y]] # You cannot make this sound cooler
    while True:
        if(canMove(moje_x + 1, moje_y, ammunation)):
            move(moje_x + 1, moje_y, ammunation)
        elif(canMove(moje_x - 1, moje_y, ammunation)):
            move(moje_x - 1, moje_y, ammunation)
        elif(canMove(moje_x, moje_y + 1, ammunation)):
            move(moje_x, moje_y + 1, ammunation)
        elif(canMove(moje_x, moje_y - 1, ammunation)):
            move(moje_x, moje_y - 1, ammunation)
        else:
            return
        print(positions['curr'])

calcPath()