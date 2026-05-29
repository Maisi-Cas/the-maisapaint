# ruff: noqa: F841
from engine.graph import *
from utils.vector2 import Vector2
from utils.print2d import Print2D as print2d
from engine.tile import Tile

class Canvas:
    def __init__(
        self,
        margin: Vector2 = Vector2(8,2),
        size: Vector2 = Vector2(48,16),
        tile: Tile = Tile(13, 12, 15, 1 )
    ):
        self.margin = margin.copy()
        self.size = size.copy()
        self.tile = tile.copy()
        
        
    def render(self, fill: bool = False):
        fillString = ''
        for i in range(self.size.x + 2):
            
            print2d.coord(
                self.margin.x + 1 + i,
                self.margin.y + 1,
                self.tile
            )
            
            print2d.coord(
                self.margin.x + 1 + i,
                self.margin.y + self.size.y + 2,
                self.tile
            )
        
        for i in range(self.size.y):
            print2d.coord(
                self.margin.x + 1,
                self.margin.y + 2 + i ,
                self.tile
            )
            
            print2d.coord(
                self.margin.x + self.size.x + 2,
                self.margin.y + 2 + i,
                self.tile
            )
            
        if fill:
            for i in range(self.size.x):
                    fillString += self.tile.getString()
            for i in range(self.size.y):
                print2d.coord(
                    self.margin.x + 2,
                    self.margin.y + 2 + i,
                    fillString
                )
                
                
            
        print(Reset.STYLE)