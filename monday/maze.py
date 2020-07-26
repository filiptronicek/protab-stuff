field = \
"""#######
#s....#
###.#.#
#c..#.#
#######"""

lines = field.split("\n")

def find(char: str):
    for iy, line in enumerate(lines):
        for ix, c in enumerate(line):
            if char == c:
                return [ix, iy]

def canMove(x, y):
 return not lines[y][x] == "#"

positions = {
    "start": find("s"),
    "endpos": find("c"),
    "currpos": find("s")
}

def move():
    curr = positions["currpos"]
    endp = positions["endpos"]
    def MvRight():
        curr = positions["currpos"]
        endp = positions["endpos"]
        nextPos = [curr[0], curr[1] + 1]
        if canMove(nextPos[0], nextPos[1]): 
            curr = nextPos
            print("Moved to "+curr)
    def MvLeft():
        curr = positions["currpos"]
        endp = positions["endpos"]
        nextPos = [curr[0], curr[1] - 1]
        if canMove(nextPos[0], nextPos[1]): 
            curr = nextPos
            print("Moved to "+curr) 
    while positions["currpos"] != positions["endpos"]:
        MvRight()
        MvLeft()
move()