import maze, time

c = maze.Connect("oof2win2", "mallet")
w = c.width
h = c.height
print(c.width, c.height)
def w():
    for i in range(c.height*10):
        c.move('w')
def aa():
    for i in range(c.height*10):
        c.move('a')
def s():
    for i in range(c.height*10):
        c.move('s')
def d():
    for i in range(c.height*10):
        c.move('d')
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