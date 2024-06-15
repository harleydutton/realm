from data.location import *
from paprika import *
from data.block import *
from procedural.generator import *


class Chunk(dict[Location,Block]):
    def prune(self, center:Location, radius: int):
        for loc in self.keys():
            if dist(center,self[loc]) > radius:
                del self[loc]
    def generate(self, center:Location, radius: int):
        g: Generator = Generator()
        for x in range(center.x-radius,center.x+radius+1):
            for y in range(center.y-radius,center.y+radius+1):
                for z in range(center.z-radius,center.z+radius+1):
                    if dist(center,Location(x,y,z))<=radius:
                        self[Location(x,y,z)]=g.generate(Location(x,y,z))
    def __str__(self) -> str:
        out: str = "Chunk@["
        for loc in self.keys():
            out=out+f"{loc},{self[loc]}] "
        return out+"]"