def moyenne(maliste):
    if len(maliste) == 0:
        return 0  # convention
    i = 0
    somme = 0  # commence à 0
    while i < len(maliste):
        somme = somme + maliste[i]
        i = i + 1
    return somme / len(maliste)

maliste = [1, 2, 3, 4, 5, 6]
sa_moyenne = moyenne(maliste)  # 3.5
print("La moyenne des éléments de ma liste est", sa_moyenne)
# ici (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5
