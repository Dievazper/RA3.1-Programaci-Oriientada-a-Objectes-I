"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Producte amb mètode per aplicar descompte.
"""

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        descompte = self.preu * (percentatge / 100)
        self.preu -= descompte
