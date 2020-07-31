import maze

c = maze.Connect("admin", "hammer")
print(c.width, c.height)

while True:
    i = input("")
    c.move(i)