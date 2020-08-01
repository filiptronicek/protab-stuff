import maze
import time     #just in case if some delay is needed, probably will not be used in the final version

#dfs for A2
#TODO:
#   [X] - get the vertexes from the function c.get_all()
#   [ ] - make the whole program work with a 2-dimensional array
#   [ ] - add function that will do the pathing

#vertex = x and y coordinates of a spot

#replace "oof2win2" with "<username>"
c = maze.Connect("oof2win2", "vylet")
area = c.get_all()

def neighbors(vertex_x, vertex_y):
    global area
    #finds the neighbors of the vertex
    #this SHOULD work. if it doesnt, it is an easy process of just rearranging the order of the appending
    n = []
    n.append(area[vertex_x][vertex_y+1])   #1
    n.append(area[vertex_x][vertex_y-1])   #2
    n.append(area[vertex_x+1][vertex_y])   #3
    n.append(area[vertex_x-1][vertex_y])   #4

    """
    #visualisation, can/should be turned off
    a1 = [9, n[3], 9]
    a2 = [n[1], 5, n[0]]
    a3 = [9, n[2], 9]
    print(*a1)
    print(*a2)
    print(*a3)
    
    #vertex_x and vertex_y = O for Origin, ! = not returned
    !4!
    2O1
    !3!
    """
    return n

def getPos(thing):
    #function that finds the object from a numberical value given and returns x, y coords of that specific (or first) object
    #chest = 3
    #wall  = 2
    #blank = 0
    height = c.height
    width  = c.width
    for i in range(height):
        for j in range(width):
            if (area[i][j] == thing):
                return [i, j]

print('pos:', getPos(3))

#should work for everything on Protab2020
def dfs(startx, starty, endx, endy):
    #finds the path from start to end in a graph using the function neighbors(). will run forever if a path doesnt exist
    visited = set()
    path = [[startx, starty]]
    while True:
        print('path:', path)
        print('neighbors:', neighbors(path[-1][0], path[-1][1]))
        done = False

        #finished
        if path[-1] == [endx, endy]:
            return path
        
        #move to different vertex, n = neighbors
        for n in neighbors(path[-1][0], path[-1][1]):
            print(n)
            if n == 0:                      #if it is a free spot
                if n not in visited:
                    visited.add(n)
                    path.append(n)
                    done = True
                    break                   #break to not move onto other unvisited neighbor
        
        if not done:                    #if a vertex that could be moved to couldn't be found, go back
            path.pop(-1)

chest = getPos(3)   #gets the x and y position of the chest
path = dfs(c.x(), c.y(), chest[0], chest[1])
#print(path)
