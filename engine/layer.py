from core.emitBus import bus
from engine.tile import Tile
from engine.panel import Panel
import engine.graph as graph
from utils.vector2 import Vector2
from utils.print2d import Print2D as print2d
from typing import Literal

class Layer:
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
 
class LayerMaster():
    def __init__(self, colorId: int, margin: Vector2, size: Vector2):
        self.colorId = colorId
        self.margin = margin.copy()
        self.size = size.copy()
        if self.size.x < 3:
            self.size.x = 3
            
        self.layer: Layer
        self.layers: list[dict] = []
        for i in range(self.size.y):
            hatsuneMiku = {}
            hatsuneMiku["name"] = f"CAPA {i}"
            hatsuneMiku["tile"] = [' ', 15, 15, 1]
            hatsuneMiku["enable"] = True
            hatsuneMiku["draw"] = {}
            self.layers.insert(0, hatsuneMiku)
        
        self.currentId = len(self.layers) - 1
        self.panel = Panel("Capas", self.colorId, self.margin - 1, self.size.copy())

    def connect(self, layer: Layer):
        if isinstance(layer, Layer):
            self.layer = layer

    def select(self, direction: Literal['u', 'd', 'l', 'r'] = 'r'):
        match direction:
            case 'u':
                if self.currentId != 0:
                    self.currentId -= 1
                else:
                    self.currentId = len(self.layers) - 1
            
            case 'd':
                if self.currentId != len(self.layers) - 1:
                    self.currentId += 1
                else:
                    self.currentId = 0
            case 'l': 
                self.layers[self.currentId]["enable"] = False
            case 'r': 
                self.layers[self.currentId]["enable"] = True
        
    def count(self, index):
        counter = {
            "char" : {},
            "fore" : {},
            "back" : {},
            "style" : {}
        }
        
        if len(self.layers[index]["draw"].values()) == 0:
            return  [" ", 15, 15, 1]
        
        for draw in self.layers[index]["draw"].values():
            char = draw[3]
            counter["char"][char] = counter["char"].get(char, 0) + 1
            fore = draw[0]
            counter["fore"][fore] = counter["fore"].get(fore, 0) + 1
            back = draw[1]
            counter["back"][back] = counter["back"].get(back, 0) + 1
            style = draw[2]
            counter["style"][style] = counter["style"].get(style, 0) + 1
        
        tile = [
            max(counter["char"], key=counter["char"].get),
            max(counter["fore"], key=counter["fore"].get),
            max(counter["back"], key=counter["back"].get),
            max(counter["style"], key=counter["style"].get)
        ]
            
        return tile
    
    def render(self):
        self.panel.render()
        colors = {
            'd' : 14,
            'ds' : 7,
            'e' : 12,
            'es' : 3
        }
        
        key: int
        
        for i in range(len(self.layers)):
            if i == self.currentId:
                if self.layers[i]["enable"]:
                    key = colors["es"]
                else:
                    key = colors["ds"]
            else:
                if self.layers[i]["enable"]:
                    key = colors["e"]
                else:
                    key = colors["d"]
            
            print2d.coord(self.margin.x + 1, self.margin.y + i + 1, graph.ForeColors[key]["color"] + ("-" * self.size.x) + graph.Reset.STYLE)
            print2d.coord(self.margin.x + 1, self.margin.y + i + 1, graph.ForeColors[key]["color"] + f"[#]{self.layers[i]["name"][:self.size.x - 3]}")
                
        
