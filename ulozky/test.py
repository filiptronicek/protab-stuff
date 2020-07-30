import maze, time

c = maze.Connect("oof2win2", "runda")

print(c.width, c.height)
for i in range(995):
    a = 'w'
    time.sleep(0.005)
    print(c.x(), c.y())
    #('direction: ')
    if a == 'w':
        c.move('w')
    elif a == 'a':
        c.move('a')
    elif a == 's':
        c.move('s')
    elif a == 'd':
        c.move('d')
    else:
        print(c.x(), c.y())
c.wait()