from core.emitBus import bus
from engine.tile import Tile
import engine.graph as graph
from utils.vector2 import Vector2
from utils.print2d import Print2D as print2d

class Draw:
    def __init__(self, margin: Vector2 = Vector2(0,0), size: Vector2 = Vector2(64,16)):
        self.margin = margin.copy()
        self.size = size.copy()
        self.pixels = {}
        bus.conect('draw-clear', self.clear)
        
    def addpixel(self, position: Vector2, tile: Tile):
        if position.x > self.size.x or position.y > self.size.y:
            return
        
        self.pixels[(position.x, position.y)] = (tile.foreColorId, tile.backColorId, tile.styleId, tile.character)
        
    def render(self):
        for (x,y),(a,b,c,d) in self.pixels.items():
            print2d.coord(
                x + self.margin.x,
                y + self.margin.y,
                (graph.ForeColors[a]['color'] + graph.BackColors[b]['color'] + graph.StyleType[c]['style'] + d + graph.Reset.STYLE)
            )
    
    def deletePixel(self, x, y):
        if (x, y) in self.pixels:
            del self.pixels[(x, y)]
            
    def clear(self):
        self.pixels = {}
        