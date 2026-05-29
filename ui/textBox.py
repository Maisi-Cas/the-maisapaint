from utils.vector2 import Vector2
from utils.print2d import Print2D as print2d
import engine.graph as graph

class TextBox:
    def __init__(self, position: Vector2, size: Vector2, content: str, idColor: int):
        self.position = position.copy()
        self.size = size.copy()
        self.idColor = idColor
        if len(content) > self.size.x * self.size.y:
            self.content = content[:self.size.x * self.size.y]
        else:
            self.content = content
            
    def render(self):
        if len(self.content) > self.size.x * self.size.y:
            self.content = self.content[:self.size.x * self.size.y]
        else:
            self.content = self.content
        print(graph.ForeColors[self.idColor]['color'])
        for i in range(self.size.y):
            if i < self.size.y - 1:
                print2d.coord(self.position.x, self.position.y + i, self.content[i * self.size.x: self.size.x * (i + 1)])
            else:
                print2d.coord(self.position.x, self.position.y + i, self.content[i * self.size.x:])
                
        print(graph.Reset.STYLE)