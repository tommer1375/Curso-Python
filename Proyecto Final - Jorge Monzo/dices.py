import random

class Dices:
    def __init__(self, dice1, dice2, wingame):
        self.dice1 = dice1
        self.dice2 = dice2
        self.wingame = wingame

class DoRoll:
    @staticmethod
    def dice_roll():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sumdice = dice1 + dice2
        wingame = sumdice == 7
        
        return dice1, dice2, sumdice, wingame

# Comprobación que hace la tirada correctamente
# dice1, dice2, sumdice, wingame = DoRoll.dice_roll()
# print(f"Dado 1: {dice1}, Dado 2: {dice2}, Suma: {sumdice}, Has ganado: {wingame}")