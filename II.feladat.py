"""
II.
Olvassunk be billentyűzetről tizedes törteket (float), és tároljuk őket egy listában!
A bevitel végét a 0.0 jelzi.
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5.5-nél nagyobb szám a listában?
2. Írjuk ki az első olyan szám indexét, ami negatív és egész (pl.: -2.0, -5.0)!
3. Hány darab 1 és 2 közé eső szám szerepel a listában?
4. Melyik volt a legnagyobb értékű negatív szám, és hányadik helyen állt?
5. Mennyi a pozitív számok összege?
"""

szamok = []
while szamok.count(0.0) == 0:
    try:
        user_input = float(input("Adj meg egy tizedes tört számot: "))
        szamok.append(user_input)
    except ValueError as e:
        print(f"{e} \nKérlek számot adj meg!")

print(szamok)
print()

szamok.remove(0.0)

#1.Volt-e 5.5-nél nagyobb szám a listában:
print("1. Volt-e 5.5-nél nagyobb szám a listában?")

for szam in szamok:
    if szam > 5.5:
        print("Igen, volt 5.5-nél nagyobb szám a listában.")
        break
else:
    print("Nem, nem volt 5.5-nél nagyobb szám a listában.")
print()

#2.Írjuk ki az első olyan szám indexét, ami negatív és egész:
print("2. Írjuk ki az első olyan szám indexét, ami negatív és egész (pl.: -2.0, -5.0)!")

try:
    for szam in szamok:
        if szam < 0 and szam % 1 == 0:
            neg_int = szam
            neg_int_index = szamok.index(neg_int) + 1
            print(f"Az első ilyen szám: {neg_int_index}")
except ValueError:
    print("Nem volt ilyen szám.")
print()