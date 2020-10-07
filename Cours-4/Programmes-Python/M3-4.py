maliste = [2, 1, -5, 8, 7, 3, 4]  # valeurs quelconques
i = 0
maxi = maliste[0]  # on initialise le max à maliste[0]
while i < len(maliste):
    if maliste[i] > maxi:
        maxi = maliste[i]
    i = i + 1
print("Le plus grand élément est :", maxi)  # ici = 8
