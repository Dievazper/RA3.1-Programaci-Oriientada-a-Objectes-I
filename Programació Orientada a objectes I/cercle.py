"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Cercle amb mètodes per calcular àrea i perímetre.
"""

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * (self.radi ** 2)

    def perimetre(self):
        return 2 * math.pi * self.radi
