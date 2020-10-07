def somme_liste(maliste):
    i = 0
    somme = 0  # commence à 0
    while i < len(maliste):
        somme = somme + maliste[i]
        i = i + 1
    return somme

maliste = [2, 1, -5, 8, 7, 3, 4]
sa_somme = somme_liste(maliste)
print("La somme des éléments de ma liste est", sa_somme)
# ici 2 + 1 + (-5) + 8 + 7 + 3 + 4 = 20
