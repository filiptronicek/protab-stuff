import maze
import time

c = maze.Connect('admin', 'velociraptor')

field = c.get_all()

inp = []

def nextPos():
    if inp[c.x() + 1] == 1 and inp[c.x() + 2] == 1 and inp[c.x() + 3] == 1 and inp[c.x() + 4] == 1: return False
    else:
        if inp[c.x() + 4] == 0:
            return False
        else:
            for i in range(4):
                if inp[c.x() + i] == 1 and inp[c.x() + 4] == 0:
                    if inp[c.x() + i + 4] == 0 and inp[c.x() + 4] == 1: return False
                    elif inp[c.x() + i + 8] == 0 and inp[c.x() + 4] == 1: return False
                    else: return True

def willHit():
    def jump():
        c.move("w")

    if inp[c.x() + 1] == 0:
        jump()
    if nextPos():
        jump()
        return True
    elif inp[c.x() + 2] == 0 and inp[c.x() + 4] == 1:
        jump()
    elif inp[c.x() + 3] == 0 and inp[c.x() + 4] == 1:
        jump()
    elif inp[c.x() + 4] == 0 and inp[c.x() + 4] == 1:
        jump()
for line in field:
    inp.append(line[-1])
print("Aiming to hit:",len(inp))

last = ""

while True:
    time.sleep(0.1)
    print(f"at {c.x()}")
    if last == c.x(): c.move("d")
    last = c.x()
    if inp[c.x() + 3] == 0 and inp[c.x() + 4] == 1:
        c.move("w")
    if inp[c.x() + 5] == 0 and inp[c.x() + 7] == 0 and inp[c.x() + 6] == 1:
        c.move("d")
        c.move("d")
        c.move("w")
    else:
        willHit()