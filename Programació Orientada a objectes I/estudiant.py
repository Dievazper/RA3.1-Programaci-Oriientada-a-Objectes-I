"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Estudiant amb mètode per comprovar si ha aprovat.
"""

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        if self.nota >= 5:
            print("Ha aprovat")
            return True
        else:
            print("No ha aprovat")
            return False
