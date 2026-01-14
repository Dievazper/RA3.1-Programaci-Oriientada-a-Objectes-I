"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Rectangle amb mètodes per calcular àrea i perímetre.
"""

class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada

    def perimetre(self):
        return 2 * (self.amplada + self.alçada)
