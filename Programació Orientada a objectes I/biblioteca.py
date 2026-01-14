"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Biblioteca per gestionar una col·lecció de llibres (afegir i mostrar).
"""

class Biblioteca:
    def __init__(self):
        self.llibres = []

    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llibres:
            llibre.mostrar_info()
