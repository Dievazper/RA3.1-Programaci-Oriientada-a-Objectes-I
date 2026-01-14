"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe Cotxe amb atributs marca, model i any, i un mètode per mostrar la informació.
"""

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Model: {self.model}, Any: {self.any}")
