# -*- coding: utf-8 -*-
# 
# Voici un petit exemple de fonction
#
def maFonction( x, y ):
    """
    maFonction(x,y) calcule 2*x + 3*y^2
    """
    # On calcule d'abord 2 x
    z1 = 2*x
    # Puis 3 y au carré
    z2 = 3*y^2
    # Puis on additionne les deux
    résultat = z1 + z2
    # Et on renvoie le résultat
    return( résultat )
# NB : les noms z1, z2 et résultats sont oubliés après appel de la fonction
