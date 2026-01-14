"""
Autor: Diego Vazquez Perez
Data: 14/01/26
Descripció: Script principal per instanciar objectes i provar les funcionalitats de totes les classes creades (Exercicis 1-10).
"""

from cotxe import Cotxe
from rectangle import Rectangle
from persona import Persona
from producte import Producte
from estudiant import Estudiant
from comptebancari import CompteBancari
from cercle import Cercle
from animal import Animal
from llibre import Llibre
from punt import Punt
from gos import Gos
from biblioteca import Biblioteca

print("--- EXERCICI 1: Cotxe ---")
# Descripció: Creant dos objectes Cotxe i mostrant la seva informació.
cotxe1 = Cotxe("Toyota", "Corolla", 2020)
cotxe2 = Cotxe("Honda", "Civic", 2019)
cotxe1.mostrar_info()
cotxe2.mostrar_info()
print()

print("--- EXERCICI 2: Rectangle ---")
# Descripció: Calculant l'àrea de tres rectangles amb diferents dimensions.
rec1 = Rectangle(5, 10)
rec2 = Rectangle(3, 7)
rec3 = Rectangle(8, 2)
print(f"Area Rec1: {rec1.area()}")
print(f"Area Rec2: {rec2.area()}")
print(f"Area Rec3: {rec3.area()}")
print()

print("--- EXERCICI 3: Estudiants Aprovats ---")
# Descripció: Verificant quins estudiants han aprovat i mostrant la seva nota.
estudiants = [
    Estudiant("Anna", 8),
    Estudiant("Joan", 4),
    Estudiant("Maria", 6),
    Estudiant("Pau", 3)
]
for est in estudiants:
    if est.ha_aprovat():
        print(f"L'estudiant {est.nom} ha aprovat amb un {est.nota}")
print()

print("--- EXERCICI 4: Compte Bancari ---")
# Descripció: Realitzant operacions d'ingrés i retirada en un compte bancari.
compte = CompteBancari(100)
compte.veure_saldo()
print("Ingressant 50...")
compte.ingressar(50)
compte.veure_saldo()
print("Retirant 30...")
compte.retirar(30)
compte.veure_saldo()
print("Retirant 200 (error)...")
compte.retirar(200)
compte.veure_saldo()
print()

print("--- EXERCICI 5: Productes Descompte ---")
# Descripció: Aplicant un descompte del 10% a una llista de productes.
def aplicar_descompte_llista(productes):
    for prod in productes:
        prod.aplicar_descompte(10)
        print(f"Nou preu {prod.nom}: {prod.preu}")

productes = [Producte("Portàtil", 1000), Producte("Ratolí", 50)]
aplicar_descompte_llista(productes)
print()

print("--- EXERCICI 6: Distància punts ---")
# Descripció: Calculant la distància entre dos punts (0,0) i (3,4).
p1 = Punt(0, 0)
p2 = Punt(3, 4)
print(f"Distància: {p1.calcular_distancia(p2)}")
print()

print("--- EXERCICI 7: Gos ---")
# Descripció: Mostrant el so genèric d'un animal i el lladruc d'un gos.
animal_generic = Animal("Bèstia", "Desconeguda")
print(f"Animal: {animal_generic.nom}")
animal_generic.fer_soroll()
gos = Gos("Rex")
print(f"Gos: {gos.nom}")
gos.fer_soroll()
print()

print("--- EXERCICI 8: Biblioteca ---")
# Descripció: Afegint llibres a una biblioteca i mostrant el catàleg.
biblio = Biblioteca()
llibre1 = Llibre("1984", "George Orwell", 1949)
llibre2 = Llibre("El Petit Príncep", "Antoine de Saint-Exupéry", 1943)
biblio.afegir_llibre(llibre1)
biblio.afegir_llibre(llibre2)
biblio.mostrar_llibres()
print()

print("--- EXERCICI 9: Cercles > 50 ---")
# Descripció: Filtrant i mostrant cercles amb àrea superior a 50.
cercles = [Cercle(2), Cercle(5), Cercle(3), Cercle(8)]
for c in cercles:
    area = c.area()
    if area > 50:
        print(f"Cercle amb radi {c.radi} té àrea {area:.2f}")
print()

print("--- EXERCICI 10: Persones > 30 anys ---")
# Descripció: Filtrant i presentant persones majors de 30 anys.
def filtrar_majors_30(persones):
    for p in persones:
        if p.edat > 30:
            p.presentar_se()

persones = [
    Persona("Carles", 25),
    Persona("Laura", 35),
    Persona("Jordi", 42),
    Persona("Marta", 20)
]
filtrar_majors_30(persones)
print()
