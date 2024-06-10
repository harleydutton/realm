from data.material import *
from data.location import *
from paprika import *
from random import *

@singleton
@data
class Generator:
    def __init__(self,seed:int=777):
        self.r=random.seed(seed)
    def generate(self,loc:Location) -> Material:
        return self.basic(loc)
    def basic(loc:Location) -> Material:
        if loc.z > 0:
            return Material.AIR
        elif random() < .5:
            return Material.STONE
        else:
            return Material.DIRT
        
            