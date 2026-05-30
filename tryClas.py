from utils.vector2 import Vector2
from ui.tileSelector import TileSelector
from ui.textBox import TextBox
from engine.table import Table
from engine.layer import LayerMaster
import msvcrt
import os

os.system("cls")
noSeQueHagConMiVida = LayerMaster(8, Vector2(4,4), Vector2(12,10))
noSeQueHagConMiVida.render()
msvcrt.getch()