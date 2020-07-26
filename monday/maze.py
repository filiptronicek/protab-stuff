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

def canMove(y, x): return not lines[y][x] == "#"

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
            positions["currpos"] = nextPos
            print("Moved to "+str(curr))
            return True
        else: return False
    def MvLeft():
        curr = positions["currpos"]
        endp = positions["endpos"]
        nextPos = [curr[0], curr[1] - 1]
        if canMove(nextPos[0], nextPos[1]):
            positions["currpos"] = nextPos
            print("Moved to "+str(curr))
            return True
        else: return False
    def MvDown():
        curr = positions["currpos"]
        endp = positions["endpos"]
        nextPos = [curr[0]+1, curr[1]]
        if canMove(nextPos[0], nextPos[1]):
            positions["currpos"] = nextPos
            print("Moved to "+str(curr)) 
            return True
        else: return False
    while positions["currpos"] != positions["endpos"]:
        if not MvRight(): MvLeft()
        MvDown()
move()