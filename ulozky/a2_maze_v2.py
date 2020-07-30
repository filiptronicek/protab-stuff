import maze
import time

c = maze.Connect('oof2win2', 'vylet')

arr = c.get_all()

width = c.width
height = c.height

visited = [[0] * (width+1)] * (height+1)

def neighbors(x, y):
    #returns the neigbors of the x y coords in an array
    #return as [[n1_x, n1_y]] etc.
    n = []
    #the following if loops are responsible for keeping the neighbors in the range of the map size
    #they go x first to let the code go from left to right first, so it doesn't just get the shortest path
    global width, height
    if x+1 < width:
        n.append([x+1, y])
    if x-1 > 0:
        n.append([x-1, y])
    if y+1 < height:
        n.append([x, y+1])
    if y-1 > 0:
        n.append([x, y-1])
    #print(n)
    return n

def find(obj):
    #function that finds the object from a numberical value given and returns x, y coords of that specific (or first) object
    #chest = 3
    #wall  = 2
    #blank = 0
    global arr

    for x in range(width):
        for y in range(height):
            if arr[x][y] == obj:
                return [x, y]       #returns the x and y coords of the object

def dfs():
    #s_x and s_y are the start x and y. g_x and g_y are the goal x and y
    s_x = c.x()
    s_y = c.y()
    g_x, g_y = find(3)
    path = [[s_x, s_y]]     #adds the starting position to the path
    visited = [[s_x, s_y]]  #a stack of places which were already visited, to not return to them

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

print(dfs())