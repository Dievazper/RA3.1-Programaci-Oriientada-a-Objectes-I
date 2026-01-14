"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Classe CompteBancari amb mètodes per ingressar, retirar i veure saldo.
"""

class CompteBancari:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def ingressar(self, quantitat):
        self.saldo += quantitat

    def retirar(self, quantitat):
        if quantitat > self.saldo:
            print("No es pot retirar. Insuficient saldo.")
        else:
            self.saldo -= quantitat

    def veure_saldo(self):
        print(f"Saldo actual: {self.saldo}")
