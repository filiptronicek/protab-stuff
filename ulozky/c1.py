import maze, time

from collections import deque

c = maze.Connect("admin", "blizko")
print(c.width, c.height)

#field = c.get_all()
field = [
    [2,0,2], 
    [2,0,2], 
    [2,0,2],
    [3,0,2]
]
keyCombos = [(0, -1, "w"), (1, 0, "d"), (0, 1, "s"), (-1, 0, "a")]

def findEnd():
    for i,f in enumerate(field):
        for j, h in enumerate(f):
            if h == 3:
                return [j, h]

def neighbors(v):
    y, x = v

    ne = []
    for k in keyCombos: 
        if 0 < y + k[1] < len(field) and 0 < x + k[0] < len(field[y]) and field[y + k[1]][x + k[0]] != 2:
            ne.append((y + k[1], x + k[0]))
            print("Appending", str((x + k[0], y + k[1])), "using", k[2])
    return nee

def bfs(start, end):
    queue = deque([start])
    beenTo = set()
    direction = dict()

    while len(queue) > 0:
        v = queue.popleft()
        print("V is", list(v))
        if v == end:
            cesta = [v]
            while v != start:
                cesta.append(direction[v])
                v = direction[v]
        else:
            ns = neighbors(v)
            for n in ns:
                if n not in beenTo:
                    queue.append(n)
                    beento.add(n)
                    direction[n] = v

print(f"Calling BFS with start {str([0,1])} and end of {str([3,0])}")
bfs([0,1], [3,0])