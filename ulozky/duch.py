import sys
import time

import maze

c = maze.Connect("admin", "jakjako")
c.wait()

def neighbors(vertex):
    #finds the neighbors of the vertex
    graph = [
        [],                 #0 - just to not need to redo most of the things here
        [2],                #1
        [1, 6, 3],          #2
        [2, 4, 5, 6, 8],    #3
        [3],                #4
        [3],                #5
        [2, 3, 7, 8],       #6
        [6, 8],             #7
        [3, 6, 7, 9, 10],   #8
        [8],                #9
        [8],                #10
    ]
    return graph[vertex]


#should work for everything on Protab2k2k
def dfs(start, end):
    #finds the path from start to end in a graph using the function neighbors(). will run forever if a path doesnt exist
    visited = set()
    path = [start]
    while True:
        done = False
        if path[-1] == end:
            return path
        #move to a different vertex
        for n in neighbors(path[-1]):
            if n not in visited:
                visited.add(n)
                path.append(n)
                done = True
                break
                
        #go back
        if not done:
            path.pop(-1)
path = dfs(1, 7)
field = c.get_all()

j = 0
for i in field:
    j += 1
    if 3 in i:
        print(f"Found it lol on {j}")