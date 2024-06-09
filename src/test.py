from data.chunk import *
from data.location import *
from data.block import *
from data.material import *
from procedural.generator import *

g: Generator = Generator()
c: Chunk = Chunk()
for x in range(10):
    for y in range(10):
        for z in range(10):
            c[Location(x=x,y=y,z=z)]=Block(g.generate())


