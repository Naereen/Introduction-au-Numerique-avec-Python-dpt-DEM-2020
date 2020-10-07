maliste = [2, 1, -5, 8, 7, 3, 4]
i = 0
selection = []
while i < len(maliste):
    if maliste[i] > 3:
        selection = selection + [maliste[i]]
    i = i + 1
print("Les élements supérieurs à 3 sont :", selection)
# ici [8, 7, 4]