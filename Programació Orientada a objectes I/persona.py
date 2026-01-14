"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Persona amb atributs nom i edat, i un mètode per presentar-se.
"""

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys")
