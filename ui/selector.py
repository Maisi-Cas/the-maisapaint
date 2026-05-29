import engine.graph as graph
from utils.vector2 import Vector2
from engine.panel import Panel
from utils.print2d import Print2D as print2d
from typing import Literal
from core.inputHandler import kInput
import random as rand
from core.emitBus import bus

class ColorSelector:
    def __init__(self, position: Vector2 = Vector2(1,1), title:str = 'ColorSelector', colorId: int = 12):
        self.position = position.copy()
        self.title = title
        self.ids = [x for x in graph.BackColors.keys()]
        self.currentId = rand.choice(self.ids)
        self.showKeys = False
        self.colorId = colorId
        self.panel = Panel(f"[{graph.ForeColors[self.currentId]['color'] + '#' + graph.Reset.STYLE}]{self.title}", self.colorId, Vector2(self.position.x, self.position.y - 2), Vector2(len(self.ids), 1))
        
    def render(self):
        self.panel.colorId = self.colorId
        self.panel.title = f"[{graph.ForeColors[self.currentId]['color'] + "#" + graph.Reset.STYLE}{graph.ForeColors[self.colorId]['color']}]{self.title}"
        
        for i in range(len(self.ids)):
            print2d.coord(self.position.x + i, self.position.y, ' ')
            
        for i in range(len(self.ids)):
            print2d.coord(self.position.x + 2 + i, self.position.y, graph.BackColors[i]['color'] + ' ' + graph.Reset.STYLE)
        self.panel.render()
        print2d.coord(self.position.x + self.currentId + 2, self.position.y + 1, graph.ForeColors[self.colorId]['color'] + '^' + graph.Reset.STYLE)

            
    def moveSelector(self, direction: Literal['l','r'] = 'r'):
        match direction:
            case 'l':
                if self.currentId != 0:
                    self.currentId -= 1
                else:
                    self.currentId = len(self.ids) - 1
            case 'r':
                if self.currentId != len(self.ids) - 1:
                    self.currentId += 1
                else:
                    self.currentId = 0
            case _:
                pass
            
class CharacterSelector:
    def __init__(self, position: Vector2 = Vector2(1,1), title:str = 'CharacterSelector', colorId: int = 12):
        self.position = position.copy()
        self.title = title
        self.ids = [x for x in graph.Characters.keys()]
        self.currentId = rand.choice(self.ids)
        self.showKeys = False
        self.colorId = colorId
        self.panel = Panel(f"[{graph.Characters[self.currentId]['character']}]{self.title}", self.colorId, Vector2(self.position.x, self.position.y - 2), Vector2(len(self.ids), 1))
        
    def render(self):
        self.panel.colorId = self.colorId
        self.panel.title = f"[{graph.Characters[self.currentId]['character']}]{self.title}"
       
        
        for i in range(len(self.ids)):
            print2d.coord(self.position.x + i, self.position.y, ' ')
            
        for i in range(len(self.ids)):
            if graph.Characters[i]['customizable']:
                print(graph.ForeColors[11]['color'])
            else:
                print(graph.ForeColors[7]['color'])
                    
            print2d.coord(self.position.x + 2 + i, self.position.y, graph.Characters[i]['character'] + graph.Reset.STYLE)
        
        self.panel.render()
        print2d.coord(self.position.x + self.currentId + 2, self.position.y + 1, graph.ForeColors[self.colorId]['color'] + '^' + graph.Reset.STYLE)
            
    def moveSelector(self, direction: Literal['l','r'] = 'r'):
        match direction:
            case 'l':
                if self.currentId != 0:
                    self.currentId -= 1
                else:
                    self.currentId = len(self.ids) - 1
            case 'r':
                if self.currentId != len(self.ids) - 1:
                    self.currentId += 1
                else:
                    self.currentId = 0
            case _:
                pass
            
    def customize(self):
        self.panel.title = f"[{graph.Characters[self.currentId]['character']}]Customizando..."
        self.panel.render()
        bus.emit('show-cmd-cursor', True)
        if graph.Characters[self.currentId]['customizable']:
            try:
                print2d.cursePos(self.position.x + 2 + self.currentId, self.position.y)
                newCharacter = input()
                graph.Characters[self.currentId]['character'] = newCharacter[0]
            except:
                pass
        bus.emit('show-cmd-cursor', False)
            
        
class StyleSelector:
    def __init__(self, position: Vector2 = Vector2(1,1), title:str = 'CharacterSelector', colorId: int = 12):
        self.position = position.copy()
        self.title = title
        self.ids = [x for x in graph.StyleType.keys()]
        self.currentId = 1
        self.showKeys = False
        self.colorId = colorId
        self.panel = Panel(self.title, self.colorId, Vector2(self.position.x, self.position.y - 2), Vector2(len(self.ids), 1))
        
    def render(self):
        self.panel.colorId = self.colorId
        self.panel.title = self.title
        
        visibleLength = 0
        styleString = ""

        for i in range(len(self.ids)):
            text = graph.StyleType[i]['name'].upper()

            if i == self.currentId:
                colored = (
                    graph.ForeColors[15]['color']
                    + graph.BackColors[2]['color']
                    + text
                    + graph.Reset.STYLE
                )
            else:
                colored = graph.ForeColors[2]['color'] + text + graph.Reset.STYLE

            if i > 0:
                styleString += ' '
                visibleLength += 1
            
            styleString += colored
            visibleLength += len(text)
            
        for i in range(visibleLength):
            print2d.coord(self.position.x + i, self.position.y, ' ')
            
        
        print2d.coord(self.position.x + 2, self.position.y, styleString)
        
        self.panel.size.x = visibleLength
        self.panel.render()
            
    def moveSelector(self, direction: Literal['l','r'] = 'r'):
        match direction:
            case 'l':
                if self.currentId != 0:
                    self.currentId -= 1
                else:
                    self.currentId = len(self.ids) - 1
            case 'r':
                if self.currentId != len(self.ids) - 1:
                    self.currentId += 1
                else:
                    self.currentId = 0
            case _:
                pass