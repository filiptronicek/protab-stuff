import maze
import random

moves = ["w", "a", "s", "d"]

c = maze.Connect('admin', 'vylet')
print('Šířka hrací plochy je', c.width)
print('Výška hrací plochy je', c.height)
moje_x = c.x()
moje_y = c.y()
print('Nacházíš se na souřadnicích', moje_x, moje_y)
print('Políčko pod tebou má hodnotu', c.get(moje_x, moje_y - 1))
print('Čekám, až klikneš na webu na tlačítko Spustit:')
c.wait()
for i in range(1000):
    if not c.move(random.choice(moves)):
        print('Posun se nepodařil, protože:', c.error)
