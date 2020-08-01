import maze, time

from collections import deque

c = maze.Connect("admin", "blizko")
print(c.width, c.height)

field = c.get_all()

keyCombos = [(0, -1, "w"), (1, 0, "d"), (0, 1, "s"), (-1, 0, "a")]

def findEnd():
    for i,f in enumerate(field):
        for j, h in enumerate(f):
            if h == 3:
                return [j, h]

def neighbors(v):
    x,y = v

    ne = []
    for k in keyCombos: 
        if 0 <= y + k[1] < len(field) and 0 <= x + k[0] < len(field[y]) and field[y + k[1]][x + k[0]] != 2:
            magicNumbers = (x + k[0], y + k[1])
            ne.append(magicNumbers)
    return ne

def bfs(start, end):
    queue = deque([start])
    beenTo = set()
    beenTo.add(tuple(start))
    direction = dict()

    while len(queue) > 0:
        v = queue.popleft()
        if list(v)  == end:
            print("doooo")
            path = [v]
            while v != start:
                path.append(direction[v])
                v = direction[v]
            return reversed(path)
            break
        else:
            ns = neighbors(v)
            for n in ns:
                if n not in beenTo:
                    queue.append(n)
                    beenTo.add(n)
                    direction[n] = v

print(f"Calling BFS with start {str([0,1])} and end of {str([3,0])}")

def move(x, y):
    for k in keyCombos:
        print("Moving")
        if c.y() + k[1] == y and c.x() + k[0] == x:
            c.move(k[2])
            break


for p in bfs([c.x(), c.y()], findEnd()):
    move(p[1], p[0])
