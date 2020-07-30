import maze, random, time

c = maze.Connect("oof2win2", "lebkoun")

p = 0
while True:
    p += 1
    i = random.choice(["a", "d", "s"])
    if i == "s":
        for i in range(5):
            c.move("w")
    else: c.move(i)