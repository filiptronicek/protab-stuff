import maze, time

from collections import deque

c = maze.Connect("admin", "nejbliz")
c.wait()
print(c.width, c.height)

field = c.get_all()
keyCombos = [(0, -1, "w"), (1, 0, "d"), (0, 1, "s"), (-1, 0, "a")]

def findEnd():
    for i,f in enumerate(field):
        for j, h in enumerate(f):
            if h == 3:
                return [j, h]

def neighbors(v):
    x, y = v

    ne = []
    for k in keyCombos:
        if field[y + k[1]][x + k[0]] != 2:
            ne.append([x + k[0], y + k[1]])
    return ne

def bfs(start, end):
    queue = deque([start])
    beenTo = set()
    direction = dict()

    while len(queue) > 0:
        v = queue.popleft()

        if v == end:
            cesta = [v]
            while v != start:
                cesta.append(direction[v])
                v = direction[v]
        else:
            queue.append(neighbors(v))
print(f"Calling BFS with start {str([c.x(), c.y()])} and end of {str(findEnd())}")
bfs([c.x(), c.y()], findEnd())