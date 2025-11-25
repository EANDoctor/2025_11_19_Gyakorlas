"""
I.
Szimuláljuk egy 6 oldalú kocka 20 dobását! A dobásokat egy listában tároljuk!
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5-ös dobás a listában?
2. Hanyadik dobás lett először 1-es?
3. Hány darab páros számot dobtunk?
4. Melyik volt a legkisebb dobás a 4-nél nagyobbak közül, és hányadik dobás volt?
5. Mennyi a 3-as dobások összege?
"""

import random as r

#Dobások:

dobasok = [r.randint(1, 6) for i in range(20)]

print("Dobások:", dobasok)
print() #Üres sor a dobások után hogy jól nézzen ki

#1.Volt-e 5-ös dobás a listában:

print("1. Volt-e 5-ös dobás a listában?")
try:
    ot_helye = dobasok.index(5) + 1
    if 5 in dobasok:
        print(f"Igen, volt 5-ös dobás, ami a(z) {ot_helye}. dobás volt.")
except ValueError:
    print("Nem, nem volt 5-ös dobás.")
print()

#2.Hanyadik dobás lett először 1-es:

print("2. Hanyadik dobás lett először 1-es?")

try:
    elso_1es_index = dobasok.index(1) + 1  #+1 mert az indexelés 1-től kezdődik
    print(f"Az első 1-es dobás a(z) {elso_1es_index}. dobás volt.")
except ValueError:
    print("Nem volt 1-es dobás.")
print()

#3.Hány darab páros számot dobtunk:

print("Hány darab páros számot dobtunk?")

try:
    paros_szamok = [pszam for pszam in dobasok if pszam % 2 == 0]
    print(f"Páros számok száma: {len(paros_szamok)}db {paros_szamok}")
except ValueError:
    print("Nincs páros dobás.")
print()

#4.Melyik volt a legkisebb dobás a 4-nél nagyobbak közül és hányadik dobás volt:

print("Melyik volt a legkisebb dobás a 4-nél nagyobbak közül, és hányadik dobás volt?")

nagyobb4 = [szam for szam in dobasok if szam > 4]
print(f"Nagyobb mint 4 dobások: {len(nagyobb4)}db {nagyobb4}")

try:
    min_nagyobb4 = min(nagyobb4)
    min4 = dobasok.index(min_nagyobb4) + 1  #+1 mert az indexelés 1-től kezdődik
    print(f"A legkisebb dobás a 4-nél nagyobbak közül: {min_nagyobb4}, amely a {min4}. dobás volt.")
except ValueError: 
    print("Nem volt 4-nél nagyobb dobás.")
print()

#5.Mennyi a 3-as dobások összege:

print("Mennyi a 3-as dobások összege?")

harom = [harom for harom in dobasok if harom == 3]
print(f"Hármas dobások: {len(harom)}db {harom}")

try:
    harom_dbszam = len(harom)
    harom_osszeg = harom_dbszam * 3
    print(f"A 3-as dobások összege: {harom_osszeg}")
except ValueError:
    print("Nincs hármas dobás.")
print()