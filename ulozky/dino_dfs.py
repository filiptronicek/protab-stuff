import sys
import time

import maze

# FIFO array of jump and run, set with 'w' and 'd'
path = []
# array of where it was tried to jump from. starts with -1 to keep the index in range
tried = []

c = maze.Connect("oof2win2", "velociraptor")
# gets the whole array and then gets only the bottom line, with 1s and 0s of land and lava
whole = c.get_all()
arr = []
for line in whole:
    arr.append(line[-1])
# arr is now the row of 1s and 0s of land and lava


def run():
    stack = dfs()
    for i in range(c.width):
        print(i)  # progress bar
        diff = stack[i + 1] - stack[i]
        if diff == 1:
            c.move("d")
        elif diff == 4:
            c.move("w")
            c.move("w")
            c.move("w")
            c.move("w")
        else:
            print("wtf")
    print("fucking done")
    return


def dfs():
    global arr
    stack = [0]  # path
    visited = [0] * 10000
    while stack != []:
        w = stack[-1]
        if w == c.width - 1:
            break
        if arr[w + 1] == 1 and visited[w + 1] == 0 and w + 1 < c.width:
            stack.append(w + 1)
            visited[w + 1] = 1
        elif arr[w + 4] == 1 and visited[w + 4] == 0 and w + 4 < c.width:
            stack.append(w + 4)
            visited[w + 4] = 1
        else:
            stack.pop(-1)
    print(stack)
    print("done")
    return stack


run()
