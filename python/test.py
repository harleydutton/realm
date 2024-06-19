from data.chunk import *
from data.location import *
from data.block import *
from data.material import *
from procedural.generator import *

c:Chunk = Chunk()
c.generate(Location(0,0,0),2)

print(c)
print(len(c.keys()))

print(c[Location(0,0,0)])
print(c[Location(0,0,1)])