import maze, random, time

c = maze.Connect("admin", "yyytyy")

p = 0
while True:
    p += 1
    i = random.choice(["a", "d", "s"])
    if i == "s":
        for i in range(5):
            time.sleep(0.1)
            c.move("w")
    else: c.move(i)