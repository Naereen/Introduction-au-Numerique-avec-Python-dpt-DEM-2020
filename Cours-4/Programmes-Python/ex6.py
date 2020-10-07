from math import sqrt  # ==> math.sqrt calcule la racine carrée

def ecart_type(maliste):
    moy = sum(maliste) / len(maliste)
    i = 0
    somme = 0  # commence à 0
    while i < len(maliste:
        somme = somme + (maliste[i] - moy)**2
        i = i + 1
    return sqrt(somme / len(maliste))

maliste = [1, 2, 3, 4, 5, 6]
son_stddev = ecart_type(maliste)  # 3.5
print("L'écart-type des éléments de ma liste est", son_stddev)
