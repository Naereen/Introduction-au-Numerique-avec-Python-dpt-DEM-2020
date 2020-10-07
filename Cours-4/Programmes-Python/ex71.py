maliste = [-5, -3, 1, 2, 3, 4, 7, 8]

# au premier appel : n = 8, milieu = 4
# gauche = [-5, -3, 1, 2] et droite = [3, 4, 7, 8]
est_present = recherche_dichotomique(maliste, 7)  # True
print(7, "est présent dans ma liste :", est_present)

est_present = recherche_dichotomique(maliste, 17)  # False
print(17, "est présent dans ma liste :", est_present)
