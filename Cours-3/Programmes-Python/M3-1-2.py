reponse = 3
proposition = int(input("Donne-moi un nombre entre 1 et 10 : "))
if proposition == reponse:               # si 1
    print("Bravo, tu as trouvé !")
elif proposition < reponse:              # sinon si 1
    print("Trop petit... Recommence")
else:                                    # sinon
    print("Trop grand... Recommence")
