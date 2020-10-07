reponse = 3
proposition = int(input("Donne-moi un nombre entre 1 et 10 : "))
if proposition == reponse:        # si 1
    print("Bravo, tu as trouvé !")
else:                             # sinon 1
    if proposition < reponse:             # si 1.1
        print("Trop petit... Recommence") # deux profondeurs
    else:                                 # sinon 1.1
        print("Trop grand... Recommence")
