"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Punt amb coordenades x, y i mètode per calcular la distància a un altre punt.
"""

import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, altre_punt):
        dx = self.x - altre_punt.x
        dy = self.y - altre_punt.y
        return math.sqrt(dx**2 + dy**2)
