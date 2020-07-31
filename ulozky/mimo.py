import maze, random, time

def do():
    try:
        c = maze.Connect("admin", "runda")

        p = 0
        while True:
            p += 1
            i = random.choice(["a", "d", "s", "w"])
            c.move(i)
            print(c.x(), c.y())
    except:
        do()
do()