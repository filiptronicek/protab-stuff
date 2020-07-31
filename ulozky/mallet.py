import maze
import time

c = maze.Connect("oof2win2", "mallet")
w = c.width
h = c.height

dir = ['d', 'a']
for i in range(h):
    line = []
    a = i % 2
    for j in range(w):
        line.append(c.get(c.x(), j))
    for j in range(w):
        if line[j] == 0:
            c.move(dir[a])
        if line[j] == 2:
            for k in range(20*5):
                c.move(dir[a])
    b = c.get(c.x, c.y+1)
    print(b)
    if b == 2:
        for k in range(20):
                c.move('s')
    if b == 0:
        c.move('s')