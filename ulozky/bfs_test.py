from collections import deque
import maze

c = maze.Connect('oof2win2', 'blizko')  

arr    = c.get_all()   #the whole map
width  = c.width
height = c.height

def neighbors(v):
    """
    #returns the neigbors of the x y coords in an array
    #return as [[n1_x, n1_y]] etc.
    n = []
    #the following if loops are responsible for keeping the neighbors in the range of the map size
    #they go x first to let the code go from left to right first, so it doesn't just get the shortest path
    global width, height, arr
    if v[0]+1 < width and arr[v[0]+1][v[1]] == 0: #if it is inside the area and is free/available
        n.append((v[0]+1, v[1]))
    if v[0]-1 > 0 and arr[v[0]-1][v[1]] == 0: 
        n.append((v[0]-1, v[1]))
    if v[1]+1 < height and arr[v[0]][v[1]+1] == 0: 
        n.append((v[0], v[1]+1))
    if v[1]-1 > 0 and arr[v[0]][v[1]-1] == 0: 
        n.append((v[0], v[1]-1))
    #print(n)
    return n
    """
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
    return graph[v+1]


def getPos(thing):
    #function that finds the object from a numberical value given and returns x, y coords of that specific (or first) object
    #chest = 3
    #wall  = 2
    #blank = 0
    height = c.height
    width  = c.width
    for i in range(height):
        for j in range(width):
            if (arr[i][j] == thing):
                return (i, j)

def bfs(start, goal):
    queue   = deque([start])
    visited = set()
    path    = dict()
    while len(queue) > 0:
        vertex = queue.popleft()
        if vertex == goal:
            print('working on path')
            theway = []
            i = len(path)
            print(path)
            while i > 0:
                a = path[i]
                theway.append(a)
                i -= 1
            return reversed(theway)
        
        #search though the 4 neigbors of the vertex and add them to the queue if they are available to go to, are not a wall
        for n in neighbors(vertex):
            if n not in visited:
                queue.append(n)
                visited.add(n)
                path[n] = vertex
    return None #if path not found, returns none


def run():
    #path = bfs((c.x(), c.y()), getPos(3))
    path = bfs(0, 10)
    if path is not None:    #if it found a path
        print('path: ', path)
        return
    else:
        print('path not found. exiting')
        return
run()