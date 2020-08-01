import maze

c = maze.Connect("admin", "jakjako")
print(c.width, c.height)

while True:
    i = input("")
    c.move(i)