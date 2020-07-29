import maze
from tqdm import tqdm
import time

c = maze.Connect('oof2win2', 'velociraptor')

field = c.get_all()

jmpLen = 4

inp = []

jumps = []

#for every line in the playing array add the bottom row of actual places where you jump on
for line in field:
    inp.append(line[-1])
print("Aiming to hit:",len(inp))

#movement functions within the live maze
def jump():
    c.move("w")
def move():
    c.move("d")

#reverses the inp list, e.g. spot 1 is 10000th and 10000th spot is 1st
r = list(reversed(inp))

print(" working on backtracking")
#while i is smaller than the length of the array
for i in range(len(r)):
    if (i < 9990):
        if (r[i+3] == 1 and r[i+7] == 1):        #there is a hole and it is not on the last spot
            #if (r[i+2] == 0):               #if 2 blocks ahead there is a hole
            jumps.append(i)    #append the location of the jump to the array, working from back to front

print('jumping in 5s')
time.sleep(5)
#finished the process of finding jumps (hopefully correctly)
def doJumps():
    global jumps
    for i in range(10000):
        x = c.x()
        time.sleep(2)
        print('att')
        if jumps[i] == x:   #if the x coordinate is a jump coordinate
            c.move("w")
            print('jumped')
        else:
            c.move('d')
            print('moved right')
print(jumps[0])
doJumps()