def indice_plus_petit(maliste):
    i = 0
    mini = maliste[0]  # on initialise le min à maliste[0]
    numero = 0         # et sa position est l'indice 0
    while i < len(maliste):
        if maliste[i] < mini:
            mini = maliste[i]
            numero = i   # nouveau mini, nouvelle position
        i = i + 1
    return numero

maliste = [2, 1, -5, 8, 7, 3, 4]
indice = indice_plus_petit(maliste)
print("Le plus petit élément de ma liste est", indice)
# ici -5 est en le plus petit, en position 2 (3ème)
