"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Animal classe base amb atributs nom i especie, i mètode genèric fer_soroll.
"""

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print("fa un soroll")
