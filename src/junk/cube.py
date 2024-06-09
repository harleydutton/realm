from paprika import *
from location import *

@data
class Block:
    loc:Location
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Block):
            return False
        return self.loc == value.loc

type BlockSet = set[Block]

# class Cusbe:
#     def __init__(self,loc):
#         self.loc=loc
#         self.mat="air" if loc[2]>0 else "dirt"
#         self.sides=[None,None,None,None,None,None] #east,north,top,west,south,bottom
#     def p(self):
#         return f"{self.mat}{self.loc}{self.sides}"
    
#     def __eq__(self, value: object) -> bool:
#         if not isinstance(value,Cube):
#             return False
#         out = True
#         for e in range(3):
#             if self.loc[e]!=value.loc[e]:
#                 out=False
#         return out
                

# def move1(n):
#     return [1 if n==0 else -1 if n==3 else 0,1 if n==1 else -1 if n==4 else 0,1 if n==2 else -1 if n==5 else 0]
# def opposite(n):
#     return (n+3)%6

# cubes_generated = 0

# def generate(start: Type[Cube], this: Type[Cube], max: float):
#     global cubes_generated
#     if dist(start.loc,this.loc) < max:
#         for n in range(6):
#             if this.sides[n] is None:
#                 temp=Cube(loc=move1(n))
#                 this.sides[n],temp.sides[opposite(n)]=temp,this
#                 cubes_generated+=1
#     for n in range(6):
#         generate(start=start,this=this.sides[n],max=max)

            
# def dir(this: Type[Cube], that: Type[Cube]):
#     pass #returns 1..6
# def join(first: Type[Cube], second:Type[Cube], first_side: int):
#     pass #split second cube to the side of the first
# def split(first: Type[Cube], second:Type[Cube]):
#     pass #remove them from each other's sides lists
