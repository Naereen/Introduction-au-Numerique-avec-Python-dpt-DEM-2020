def plus_petit(maliste):
    i = 0
    mini = maliste[0]  # on initialise le min à maliste[0]
    while i < len(maliste):
        if maliste[i] < mini:
            mini = maliste[i]
        i = i + 1
    return mini

maliste = [2, 1, -5, 8, 7, 3, 4]
son_plus_petit = plus_petit(maliste)
print("Le plus petit élément de ma liste est", son_plus_petit)
# ici -5
