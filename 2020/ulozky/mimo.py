import maze, random, time
from tqdm import tqdm

def do():
    c = maze.Connect("admin", "runda")
    p = 0
    for i in tqdm(range(1_000_001)):
        p += 1
        if p > 1_000_000:
            while True:
                c.move("a")
        else:
            i = random.choice(["a", "d", "s", "w"])
            c.move(i)

do()