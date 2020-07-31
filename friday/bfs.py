from collections import deque

def neighbors(v):
    pass # Tůdů

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
            direction[v] = v