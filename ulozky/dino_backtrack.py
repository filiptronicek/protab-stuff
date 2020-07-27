import maze
from tqdm import tqdm
import time

c = maze.Connect('admin', 'velociraptor')

field = c.get_all()

jmpLen = 4

inp = []
comms = [[10000, 0]]
now = comms[0][0]
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
        lastNodeIndex = now - jmpLen + i
        lastNode = inp[lastNodeIndex] 

        leftNodeIndex = now - jmpLen - 1 + i
        leftNode = inp[leftNodeIndex]

        if leftNode == 1:
            now = leftNodeIndex
            comms.append([leftNodeIndex, 0])

            break
        else:
            if lastNode == 1:
                now = lastNodeIndex
                comms.append([lastNodeIndex, 1])
                break
            else:
                comms.append([lastNodeIndex, 0])

print(comms)
c.wait()
"""
while True:
    print(f"If {c.x()} in comms")
    if c.x() in comms:
        print("Yes")
        jump()
    else:
        move()
"""