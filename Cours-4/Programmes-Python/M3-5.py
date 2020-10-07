maliste = [2, 1, -5, 8, 7, 3, 4]  # valeur quelconque
i = 0
maxi = maliste[0]  # on initialise le max à maliste[0]
numero = 0         # et sa position est l'indice 0
while i < len(maliste):
    if maliste[i] > maxi:
        maxi = maliste[i]
        numero = i   # nouveau maxi, nouvelle position
    i = i + 1
print("Le numéro du plus grand élément est :", numero)
# ici, numero = 3 car maxi = 8 en position 3
