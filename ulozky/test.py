import maze, time

c = maze.Connect("oof2win2", "mallet")
w = c.width
h = c.height
print(c.width, c.height)
while True:
    a = input('dir: ')
    if a == 'a':
        c.move('a')
    elif a == 'w':
        c.move('w')
    elif a == 's':
        c.move('s')
    elif a == 'd':
        c.move('d')
    elif a == 'aa':
        aa()
    elif a == 'ww':
        w()
    elif a == 'ss':
        s()
    elif a == 'dd':
        d()