from enum import Enum

class States(Enum):
    DRAW = 0
    SELECTCOLOR = 1
    
current = States.DRAW 

isRendering:bool = True
clockIsRendering:bool = False