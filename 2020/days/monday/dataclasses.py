from dataclasses import dataclass

@dataclass
class Entity:
    y: int
    x: int

e = Entity(x=1, y=2)
f = Entity(x=2, y=2)
print(e == f)