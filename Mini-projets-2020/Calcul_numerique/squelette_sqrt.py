#!/usr/bin/env python
# coding: utf-8

# Dernier TP (mini projet) : exemples de calcul numérique
# - Prof : Lilian Besson
# - Site du cours : [https://perso.crans.org/besson/teach/intro_num_DEM_2020/](https://perso.crans.org/besson/teach/intro_num_DEM_2020/)
# - Date : mercredi 14/10/2020 et vendredi 16/10/2020.

# ----
# ## Racine carrée $x \mapsto \sqrt{x}$
#
# L'algorithme pour calculer une valeur approchée de la racine carrée d'un nombre réel positif $a$ est le suivant :
#
# - on commence par trouver une valeur approchée entière qui soit la plus proche possible. Mathématiquement, on peut calculer par exemple $x_0 = \lceil \sqrt{a} \rceil$ la partie entière supérieure de $\sqrt{a}$. C'est très rapide avec une simple boucle `while` :
#
# ```python
#     sqrt_a_entiere = 0
#     while sqrt_a_entiere**2 < a:
#         # tant qu'on peut augmenter sqrt_a_entiere on le fait
#         sqrt_a_entiere = sqrt_a_entiere + 1
#     # sqrt_a_entiere est le plus petit entier tel que sqrt_a_entiere**2 >= a
#     # c'est un bon début pour une valeur approchée sqrt(a) qui deviendra plus précise
# ```
#
# - le premier terme de la suite $x_n$ sera ce $x_0$ que l'on vient de calculer (en fait n'importe quelle valeur $x_0>0$ fonctionne mais autant essayer de partir d'une valeur proche de l'objectif),
# - ensuite on *itère* le calcul suivant : $$x_{n+1} = (x_n + a/x_n) / 2, (\star)$$ jusqu'à ce que $x_n$ soit assez proche de $\sqrt{a}$, c'est à dire jusqu'à ce que $|x_n^2 - a|$ soit assez petit (valeur absolue de la différence). (pour les curieux-ses : on dit que la suite $(x_n)$ ($\star$) est récurrente d'ordre 1, car $x_n$ dépend de $x_{n-1}$ uniquement)
# - on peut aussi décider à l'avance de s'arrêter après un certain nombre d'itérations, par exemple $N=10$. Cet algorithme est très rapide pour calculer avec une bonne précision les premières décimales - nombres avec la virgule - de la valeur objectif $\sqrt{a}$, donc même une petite valeur comme $N=10$ suffira !
# - Note : pour calculer le $n$-ième terme de cette suite récurrente ($\star$), on n'a pas besoin de stocker toutes les valeurs, donc pas besoin d'imaginer avoir plein de variables $x_0, x_1, x_2, ..., x_n$ ou de les stocker dans une liste. On peut utiliser une seule variable $x_n$ que l'on met à jour. Le calcul est fait avec une simple boucle `while` :
#
# ```python
#     N = 10             # nombre maximum d'itérations, peut être plus grand
#     n = 0              # nombre d'itération, augmente de 1 dans chaque passage du while
#     x_n = x_0          # valeur initiale de l'approximation x_n de sqrt(a)
#     while n < N:       # tant qu'on a encore des itérations possibles
#         x_n = ...          # on applique la formule de la récurrence (⋆)
#         n = n + 1          # et on continue avec n+1
# ```
#
# *Point Culture* : cette méthode numérique est appelée [méthode de Héron](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_H%C3%A9ron), car elle a d'abord été d'abord attribuée au mathématicien grec Héron (1er siècle après J-C), mais elle date de bien plus longtemps, des Babyloniens (-2000 av J-C) et des Égyptiens.

# ##### Pour les plus curieux-ses
# > En fait, cette méthode est un cas particulier d'un algorithme plus générique, qui s'appelle la méthode de Newton (ou Newton-Raphson) pour calculer une approximation d'une solution à une équation de type $g(x) = 0$ pour une fonction "gentille" $g$ (ie. continue et dérivable et de dérivée continue).
# > Appliquer la méthode (générale) de Newton à la fonction objectif $g(x) = x^2 - a$, dont le zéro est $x=\sqrt{a}$ (en effet $g(x) = 0 \Leftrightarrow x = \sqrt{a}$), donne le même algorithme.
# >
# > - $x_0$ est pris dans le domaine de $g$ et ensuite on itère $x_{n+1} = x_n - g(x_n) / g'(x_n)$.
# > - Référence : https://fr.wikipedia.org/wiki/Méthode_de_Newton#Racine_carrée

# ##### L'exercice
#
# Inspirez vous du squelette de code ci dessous, où les `...` signifient que vous devez ajouter du code, et écrivez une fonction `sqrt(x)` qui calcule l'algorithme décrit plus haut.
#
# Ensuite, testez la avec des valeurs connues :
#
# - pour $a$ un entier, `sqrt(a*a)` doit donner $a$ (et vous devez probablement connaître de tête que $\sqrt{16}=4$, $\sqrt{25}=5$ etc),
# - pour $a$ un nombre flottant (réel), `sqrt(a*a)` doit donner $a$.


def sqrt(a):
    """ Approximation de sqrt(a) avec la méthode de Héron et N=10 étapes."""
    # 1) calculer une première approximation de sqrt(a)
    #    sqrt_a_entiere = ceil(sqrt(a)) (partie entière supérieure)
    sqrt_a_entiere = 0.0
    x_0 = ...  # valeur initiale

    # 2) maintenant la méthode Héron que l'on itère un certain nombre de fois
    N = 10  # nombre maximum d'étapes, que l'on peut augmenter
            # pour gagner en précision si besoin
    n = ...
    x_n = x_0

    while n < N:

        # pour voir l'évolution du calcul, décommentez la ligne ci dessous
        # c'est à dire enlevez le # en début de ligne
        print("  Calcul de sqrt(", a, "), n =", n, "et x_n =", x_n)

        # maintenant le calcul
        n = n + 1
        ...   # /!\ à vous d'écrire quelque chose ici
    return x_n


# ##### Exemples avec des valeurs entières

b = 2
while b <= 10:
    a = b*b
    print("Calcul de sqrt(", a, ") :")
    sqrt_a = sqrt(a)
    print("Notre fonction sqrt a calculé sqrt(b*b) =", sqrt_a, "pour b =", b)
    b = b + 3


# - Question : Commentez.
# - Question : A-t-on utilisé la formule de mise à jour de $x_n$ (formule de Héron ($\star$)) pour calculer ces racines carrées ?
# - Question : Est-ce qu'on aurait pu s'arrêter plus tôt que ces `N=10` itérations de la suite $(\star$) ?

# ##### Exemples avec des valeurs flottantes


b = 0.25
while b <= 5:
    a = b*b
    print("Calcul de sqrt(", b, ") :")
    sqrt_a = sqrt(a)
    print("Notre fonction sqrt a calculé sqrt(b*b) =", sqrt_a, "pour b =", b)
    b = b + 1.5


# Vous pouvez peut-être voir des (petites) erreurs de calcul, avec des exemples pour $a$ flottant.

# ##### Une version plus compliquée
#
# Ici, je vous donne le code d'un squelette un peu plus compliqué, avec des `...` à remplir aux mêmes endroits.
#
# - Question : Expliquer la modification. (`abs(x)` =$|x|$ calcule la valeur absolue de $x$)


def sqrt(a):
    """ Approximation de sqrt(a) avec la méthode de Héron et N=10 étapes."""
    # 1) calculer une première approximation de sqrt(a)
    ...  # même code qu'avant pour calculer x_0

    # 2) maintenant la méthode Héron que l'on itère un certain nombre de fois
    ...  # même code qu'avant pour initialiser n, N et x_n

    precision = 1e-12   # c'est égal à 10^{-12}, exemple de précision
    while abs(x_n**2 - a) > precision and n < N:
        # note : abs(x) = |x| calcule la valeur absolue de x
        ...  # même code qu'avant pour mettre à jour x_n et n
    return x_n


# - Question : Essayez cette version sur les exemples précédents.
# - Question : Est-ce qu'elle termine plus rapidement (sans faire des itérations de la suite ($\star$) inutiles) ?

# ##### Bonus :  calculer $\sqrt[m]{a}$ pour $m$ entier quelconque
#
# Je ne donne pas tous les détails, mais pour calculer une racine $m$-ième au lieu d'une racine carrée, une méthode similaire peut être utilisée :
#
# - on commence par trouver une valeur approchée entière qui soit la plus proche possible. Mathématiquement, on calcule $x_0 = \lceil \sqrt[m]{a} \rceil$ la partie entière supérieure de $\sqrt[m]{a}$ :
#
# ```python
#     sqrt_m_a_entiere = 0
#     while sqrt_m_a_entiere ** m < a:  # **m et plus **2
#         sqrt_m_a_entiere = sqrt_m_a_entiere + 1
# ```
#
# - ensuite on itère le calcul suivant : $x_{n+1} = (1/m) * ((m-1) * x_n + a / x_n^{m-1})$, jusqu'à ce que $x_n$ soit assez proche de $\sqrt[m]{a}$, c'est à dire jusqu'à ce que $|x_n^m - a|$ soit assez petit (valeur absolue de la différence).


def sqrt_generale(x, m):
    """ Approximation de sqrt[m](a) avec la méthode de Héron et N=10 étapes."""
    # 1) calculer une première approximation de sqrt[m](a)
    ...  # même code qu'avant pour calculer x_0

    # 2) maintenant la méthode Héron que l'on itère un certain nombre de fois
    ...  # même code qu'avant pour initialiser n, N et x_n

    epsilon = 1e-12   # c'est égal à 10^{-12}
    while (x_n**2 - a) > epsilon and n < N:
        x_n = ((m-1.0)*x_n + x / x_n**(m-1)) / m
        ...  # même code qu'avant pour mettre à jour n
    return x_n

print("Vous devez remplir le fichier et faire l'exercice")
print("Fin du fichier squelette_sqrt.py")
