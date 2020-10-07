def nb_occurrences(maliste, valeur):
    i = 0
    nombre = 0  # commence à 0
    while i < len(maliste):
        if maliste[i] == valeur:
            nombre = nombre + 1
        i = i + 1
    return nombre

maliste = ['J', 'u', 'l', 'e', 's', 'C', 'e', 's', 'a', 'r']
nombre_de_e = nb_occurrences(maliste, 'e')
print("La nombre de 'e' dans ma liste est", nombre_de_e)
# ici = 2 pour 'e' dans Jules et 'e' dans Cesar
