import maze
import time

c = maze.Connect('admin', 'velociraptor')

field = c.get_all()

jmpLen = 4

inp = []
jumps = [10000  ]

for line in field:
    inp.append(line[-1])
print("Aiming to hit:",len(inp))

def jump():
    c.move("w")
def move():
    c.move("d")

r = list(reversed(inp))

while jumps[-1] > jmpLen:
    if inp[jumps[-1] - jmpLen] == 1:
        jumps.append(inp[jumps[-1] - jmpLen])
print(jumps)