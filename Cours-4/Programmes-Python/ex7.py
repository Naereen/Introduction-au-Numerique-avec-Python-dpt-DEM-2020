def recherche_dichotomique(maliste, valeur):
    n = len(maliste)
    if n == 0:  # aucune valeur dans liste vide
        return False
    milieu = n // 2  # position au milieu
    if valeur == maliste[milieu]:
        return True  # trouvé !
    elif valeur < maliste[milieu]:
        # il faut rechercher à gauche
        gauche = maliste[0 : milieu]
        return recherche_dichotomique(gauche, valeur)
    else:  # valeur > maliste[milieu]
        # il faut rechercher à droite
        droite = maliste[milieu : n]
        return recherche_dichotomique(droite, valeur)
