import maze
import time     #just in case if some delay is needed, probably will not be used in the final version

#dfs for A2
#TODO:
#  [X] - get the vertexes from the function c.get_all()
#  [ ] - make the whole program work with a 2-dimensional array
#  [ ] - add function that will do the pathing

#vertex = x and y coordinates of a spot

#replace "oof2win2" with "<username>"
c = maze.Connect("oof2win2", "vylet")

def neighbors(vertex_x, vertex_y):
    #finds the neighbors of the vertex
    graph = c.get_all()
    n = []
    n.append(graph[vertex_x][vertex_y+1])
    n.append(graph[vertex_x][vertex_y-1])
    n.append(graph[vertex_x+1][vertex_y])
    n.append(graph[vertex_x-1][vertex_y])
    return n

print(neighbors(c.x(), c.y()))

#should work for everything on Protab2020
def dfs(startx, starty, endx, endy):
    #finds the path from start to end in a graph using the function neighbors(). will run forever if a path doesnt exist
    visited = set()
    path = [[startx, starty]]
    while True:
        done = False

        #finished
        if path[-1] == [endx, endy]:
            return path
        
        #move to different vertex, n = neighbors
        for n in neighbors(path[-1][0], path[-1][1]):
            if n == 0:                      #if it is a free spot
                if n not in visited:
                    visited.add(n)
                    path.append(n)
                    done = True
                    break                   #break to not move onto other unvisited neighbor
        
        if not done:                    #if a vertex that could be moved to couldn't be found, go back
            path.pop(-1)
#path = dfs(c.x(), c.y())
#print(path)
