import maze
import time

c = maze.Connect('oof2win2', 'vylet')

arr = c.get_all()

width = c.width
height = c.height

visited = [[0] * (width+1)] * (height+1)

def neighbors(v):
    #returns the neigbors of the x y coords in an array
    #return as [[n1_x, n1_y]] etc.
    n = []
    #the following if loops are responsible for keeping the neighbors in the range of the map size
    #they go x first to let the code go from left to right first, so it doesn't just get the shortest path
    global width, height, arr
    if v[0]+1 < width and arr[v[0]+1][v[1]] != 2: #if it is inside the area and is free/available
        n.append((v[0]+1, v[1]))
    if v[0]-1 >= 0 and arr[v[0]-1][v[1]] != 2: 
        n.append((v[0]-1, v[1]))
    if v[1]+1 < height and arr[v[0]][v[1]+1] != 2: 
        n.append((v[0], v[1]+1))
    if v[1]-1 >= 0 and arr[v[0]][v[1]-1] != 2: 
        n.append((v[0], v[1]-1))
    #print(n)
    return n

def getPos(thing):
    #function that finds the object from a numberical value given and returns x, y coords of that specific (or first) object
    #chest = 3
    #wall  = 2
    #blank = 0
    global arr, width, height

    for x in range(width):
        for y in range(height):
            if arr[x][y] == thing:
                return (x, y)       #returns the x and y coords of the object

def dfs():
    #s_x and s_y are the start x and y. g_x and g_y are the goal x and y
    s_x = c.x()
    s_y = c.y()
    g_x, g_y = getPos(3)
    path = [(s_x, s_y)]     #adds the starting position to the path
    visited = [(s_x, s_y)]  #a stack of places which were already visited, to not return to them

    while True:             #while path not found
        x = c.x()
        y = c.y()
        if path[-1][0] == g_x and path[-1][1] == g_y:   #last position of path is goal
            return path
        for n in neighbors(x, y):
            if n is not visited:            #if the position has not been visited
                if c.get(n[0], n[1]) != 2:  #if the position isnt a wall
                    visited.append(n)
                    path.append(n)
                    break
        else:                               #if there is no other option than going back
            path.pop(-1)

def doPath(path):
    prev = 0
    now = 1
    while now < len(path):
        dx = path[now][0] - path[prev][0]
        dy = path[now][1] - path[prev][1]
        time.sleep(0.05)
        print(dx, dy)

        if dx == 1:
            c.move('d')
        if dx == -1:
            c.move('a')
        if dy == 1:
            c.move('s')
        if dy == -1:
            c.move('w') 
        
        prev += 1
        now  += 1
    return

def run():
    print('searching to:', getPos(3))
    path = dfs()
    #path = bfs(6, 9)
    if path is not None:    #if it found a path
        print('path: ', path)
        doPath(path)
        return
    else:
        print('path not found. exiting')
        return
run()