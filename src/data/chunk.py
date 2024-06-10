from data.location import *
from paprika import *
from data.block import *

@data
class Chunk(dict[Location,Block]):
    pass