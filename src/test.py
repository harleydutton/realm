from data.chunk import *
from data.location import *
from data.block import *
from data.material import *
from procedural.generator import *

g: Generator = Generator()
c: Chunk = Chunk()
for x in range(-1,2):
    for y in range(-1,2):
        for z in range(-1,2):
            c[Location(x,y,z)]=Block(g.generate(Location(x,y,z)))

print(c)
print(len(c.keys()))

print(c[Location(0,0,0)])
print(c[Location(0,0,1)])