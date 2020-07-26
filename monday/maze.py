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
print(positions)