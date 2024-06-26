from math import sqrt
from paprika import *

# +z is up, +x is north
@data
class Location:
    x: int
    y: int
    z: int
    def __str__(self):
        return f"Loc@][{self.y},{self.x},{self.z}]"

class RelativeLocation(Location):
    pass

def dist(a: Location, b: Location):
    return sqrt((a.x-b.x)**2+(a.y-b.y)**2+(a.z-b.z)**2)
