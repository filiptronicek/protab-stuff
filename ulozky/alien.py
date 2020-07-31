import maze
import time

def do():
        c = maze.Connect('oof2win2', 'emzak')

        while True:
            for i in range(c.height):
                for i in range(c.width - 2):
                    c.move('w')
                    c.move('w')
                    c.move('d')
                for i in range(c.width - 2):
                    c.move('w')
                    c.move('w')
                    c.move('a')
do()
