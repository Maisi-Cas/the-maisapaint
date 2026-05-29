import engine.graph as graph

class Tile:
    def __init__(self, characterID, foreColorID, backColorID, styleID):
        self.characterId = characterID
        self.character = graph.Characters[characterID]['character']
        self.foreColorId = foreColorID
        self.backColorId = backColorID
        self.styleId = styleID
    
    def changeCharId(self, id):
        self.characterID = id
        self.character = graph.Characters[id]['character']
    
    def __str__(self):
        return graph.ForeColors[self.foreColorId]['color'] + graph.BackColors[self.backColorId]['color'] + graph.StyleType[self.styleId]['style'] + self.character + graph.Reset.STYLE
    
    def getString(self):
        return graph.ForeColors[self.foreColorId]['color'] + graph.BackColors[self.backColorId]['color'] + graph.StyleType[self.styleId]['style'] + self.character + graph.Reset.STYLE
    
    def copy(self):
        return Tile(self.characterId, self.foreColorId, self.backColorId, self.styleId)