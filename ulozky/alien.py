import maze
import time

def do():
    try:
        c = maze.Connect('admin', 'lebkoun')

        while True:
            for i in range(c.height):
                for i in range(c.width - 2):
                    c.move('w')
                    c.move('w')
                    c.move('d')
                    time.sleep(0.05)
                for i in range(c.width - 2):
                    c.move('w')
                    c.move('w')
                    c.move('a')
                    time.sleep(0.05)
    except:
        do()
do()