import sys, time
from tqdm import tqdm

import maze

# FIFO array of jump and run, set with 'w' and 'd'
path = []
# array of where it was tried to jump from. starts with -1 to keep the index in range
tried = []

c = maze.Connect("admin", "archeopteryx")


# gets the whole array and then gets only the bottom line, with 1s and 0s of land and lava
whole = c.get_all()
arr = []
for line in whole:
    arr.append(line[-1])
# arr is now the row of 1s and 0s of land and lava

def move(type: str, amnt: int):
    key = ""
    if type == 'jump': key = "w"
    elif type == 'walk': key = "d"
    for i in range(amnt):
        c.move(key)

def run():
    stack = dfs()
    for i in tqdm(range(c.width-100)):
        time.sleep(0.05)
        diff = stack[i + 1] - stack[i]
        if diff == 1:
            c.move("d")
        elif diff == 4:
            c.move('w')
            move("walk", 3)
        elif diff == 6:
            c.move('w')
            c.move('w')
            move("walk", 4)
        elif diff == 8:
            c.move('w')
            c.move('d')
            c.move('w')
            move("walk", 5)
        else:
            print("wtf")
    print("fucking done")
    c.wait()
    return

def dfs():
    global arr
    stack = [0]  # path
    visited = [0] * 10000
    while stack != []:
        w = stack[-1]
        if w == c.width - 1:
            break
        if w + 1 < c.width and arr[w + 1] == 1 and visited[w + 1] == 0:
            stack.append(w + 1)
            visited[w + 1] = 1  
        elif w + 4 < c.width and arr[w + 4] == 1 and visited[w + 4] == 0:
            stack.append(w + 4)
            visited[w + 4] = 1
        elif w + 6 < c.width and arr[w + 6] == 1 and visited[w + 6] == 0:
            stack.append(w + 6)
            visited[w + 6] = 1
        elif w + 8 < c.width and arr[w + 8] == 1 and visited[w + 8] == 0:
            stack.append(w + 8)
            visited[w + 8] = 1
        else:
            stack.pop(-1)
    print(stack)
    print("done")
    return stack

run()
