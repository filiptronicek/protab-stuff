import maze
from tqdm import tqdm
import time

c = maze.Connect('admin', 'velociraptor')

field = c.get_all()

jmpLen = 4

inp = []
comms = [10000]
now = comms[0]
for line in field:
    inp.append(line[-1])
print("Aiming to hit:",len(inp))

def jump():
    c.move("w")
def move():
    c.move("d")

r = list(reversed(inp))

for g in range(len(inp)):
    if now < 0: break
    for i in range(jmpLen):
        print("Counting for",now)
        lastNodeIndex = now - jmpLen - i
        lastNode = inp[lastNodeIndex] 

        leftNodeIndex = now - jmpLen - 1 - i
        leftNode = inp[leftNodeIndex]
        if leftNode == 1:
            now = leftNodeIndex
        else:
            if lastNode == 1:
                now = lastNodeIndex
                comms.append(now - jmpLen - i)
                break
print(comms)
for p in range(len(inp)):
    time.sleep(0.5)
    if p in comms:
        jump()
    else:
        move()
