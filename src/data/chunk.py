from location import *
from paprika import *
from block import *

@data
class Chunk(dict[Location,Block]):
    pass