"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Gos que hereta d'Animal i sobreescriu el mètode fer_soroll.
"""

from animal import Animal

class Gos(Animal):
    def __init__(self, nom, especie="Gos"):
        super().__init__(nom, especie)

    def fer_soroll(self):
        print("Bup bup!")
