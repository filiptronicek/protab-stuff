import maze
import time

c = maze.Connect('oof2win2', 'vylet')

while True:
    a = input('input: ')
    if a == 'w':
        c.move('w')
    elif a == 'a':
        c.move('a')
    elif a == 's':
        c.move('s')
    elif a == 'd':
        c.move('d')