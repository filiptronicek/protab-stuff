import maze, time
from getkey import getkey, keys

c = maze.Connect("oof2win2", "runda")
c.wait()
print(c.width, c.height)
while True:
    key = getkey()
    if key == keys.LATIN_SMALL_LETTER_W:
        c.move('w')
    elif key == keys.LATIN_SMALL_LETTER_A:
        c.move('a')
    elif key == keys.LATIN_SMALL_LETTER_S:
        c.move('s')
    elif key == keys.LATIN_SMALL_LETTER_D:
        c.move('d')