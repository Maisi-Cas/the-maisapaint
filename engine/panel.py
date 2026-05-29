import engine.graph as graph
from utils.vector2 import Vector2
from utils.print2d import Print2D as print2d

class Panel:
    def __init__(self, title: str, colorId: int, margin: Vector2, size: Vector2):
        self.title = title
        self.colorId = colorId
        self.margin = margin.copy()
        self.size = size.copy()
        
    def render(self, clear: bool = False):
        # Aplicamos color
        print(graph.ForeColors[self.colorId]['color'])
        
        # Comenzamos a imprimir las esquinas
        string = '┌┐└┘─│'
        
        print2d.coord(
            self.margin.x + 1,
            self.margin.y + 1,
            '┌'
        )
        print2d.coord(
            self.margin.x + self.size.x + 2,
            self.margin.y + 1,
            '┐'
        )
        print2d.coord(
            self.margin.x + 1,
            self.margin.y + self.size.y + 2,
            '└'
        )
        print2d.coord(
            self.margin.x + self.size.x + 2,
            self.margin.y + self.size.y + 2,
            '┘'
        )

        for i in range(self.size.x):
            print2d.coord(
                self.margin.x + 2 + i,
                self.margin.y + 1,
                '─'
            )
            print2d.coord(
                self.margin.x + 2 + i,
                self.margin.y + self.size.y + 2,
                '─'
            )
            
        for i in range(self.size.y):
            print2d.coord(
                self.margin.x + 1,
                self.margin.y + 2 + i,
                '│'
            )
            print2d.coord(
                self.margin.x + self.size.x + 2,
                self.margin.y + 2 + i,
                '│'
            )
            
        print2d.coord(
            self.margin.x + 3,
            self.margin.y + 1,
            self.title
        )
        print(graph.Reset.STYLE)
        
        if clear:
            fillString = ''
            for _ in range(self.size.x):
                fillString += ' '
            for i in range(self.size.y):
                print2d.coord(self.margin.x + 2, self.margin.y + 2 + i, fillString)