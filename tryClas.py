from utils.vector2 import Vector2
from ui.tileSelector import TileSelector
from ui.textBox import TextBox
from engine.table import Table
import msvcrt
import os

os.system("cls")

table = Table("Prepucio", 12, Vector2(5,5), 4, 15)
table.setHeadings("Hola", "Prepummmmcio", "XD", "Jaja")
table.addContet("Suco", "Me", "La Pela", "Deja la paja")
table.addContet("Increible", "Lo logre", "Carajo hermano", "Soy dios")
table.setColors([2],[2,3,4,8])
table.setRowSize(4)
table.show()