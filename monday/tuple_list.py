import sys

y = [x for x in range(10) if x % 3 == 0]
yt = {x for x in range(10) if x % 3 == 0}

print(y)
print(yt)

print({2**i: i for i in range(40) if 2**i < 9223372036854775807})

print(sys.maxsize)