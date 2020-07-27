import maze
import time

c = maze.Connect('admin', 'velociraptor')

field = c.get_all()

jmpLen = 4

inp = []
jumps = [10000]

for line in field:
    inp.append(line[-1])
print("Aiming to hit:",len(inp))

def jump():
    c.move("w")
def move():
    c.move("d")

r = list(reversed(inp))

for i,j in enumerate(inp):
    if inp[jumps[-1] - jmpLen - i] == 1:
        jumps.append(jumps[-1] - jmpLen - i)
        print(jumps)
        break

print(jumps)