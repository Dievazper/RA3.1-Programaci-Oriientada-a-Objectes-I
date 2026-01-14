"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Llibre amb atributs títol, autor i any. Mètode per mostrar informació.
"""

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Any: {self.any}")
