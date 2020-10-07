def produit_liste(maliste):
    i = 0
    produit = 1  # commence à 1
    while i < len(maliste):
        produit = produit * maliste[i]
        i = i + 1
    return produit

maliste = [1, 2, 3, 4, 5, 6]
son_produit = produit_liste(maliste)  # 720
print("La produit des éléments de ma liste est", son_produit)
# ici 1 * 2 * 3 * 4 * 5 * 6 = 720
