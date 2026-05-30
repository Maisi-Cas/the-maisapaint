import os
import msvcrt

class Print2D:
    def __init__(self):
        pass
    
    def coord(x: int = 1, y: int  = 1, string: str = 'Lorem Ipsum!'):
        if x <= 0 or y <= 0:
            return
        print(f"\033[{y};{x}H{string}")
        
    def cursePos(x: int = 1, y: int = 1):
        if x <= 0 or y <= 0:
            return
        print(f"\033[{y};{x}H", end='')
        
    def clear():
        os.system('cls')
        
    def debugPrint(string: str):
        os.system('cls')
        print(string)
        msvcrt.getch()