def neighbors(v):
    pass
def dfs():
    path = []
    beenTo = set()

    while len(path) > 0:
        v = path[-1]
        beenTo.add(v)

        for n in neighbors(v):
            if not n in beenTo:
                path.append(n)
                break
        else:
            path.pop()