import maze
import time
from collections import Counter

c = maze.Connect('oof2win2', 'velociraptor')
print('gettig area')
field = c.get_all()

inp = []
options = []
#for every line in the playing array add the bottom row of actual places where you jump on
for line in field:
    inp.append(line[-1])
print('collecting options')
for i in range(len(inp)):
    if inp[i] == 0:
        out = []
        string = ""
        if (9992 <= i):
            break
        for j in range(8):
            out.append(inp[i+j])
        print(out)
        for j in range(len(out)):
            string = ''.join(str(out))
        i += 8
print(options)
print(Counter(options))