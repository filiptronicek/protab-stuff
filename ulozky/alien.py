import maze
import time

c = maze.Connect('oof2win2', 'lebkoun')

while True:
    for i in range(c.height):
        for i in range(c.width):
            c.move('w')
            c.move('w')
            c.move('d')
            time.sleep(0.05)
        for i in range(c.width):
            c.move('w')
            c.move('w')
            c.move('a')
            time.sleep(0.05)