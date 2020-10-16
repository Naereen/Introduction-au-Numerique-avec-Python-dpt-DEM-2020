#!/usr/bin/env python
# coding: utf-8

# Dernier TP (mini projet) : exemples de calcul numérique
# - Prof : Lilian Besson
# - Site du cours : [https://perso.crans.org/besson/teach/intro_num_DEM_2020/](https://perso.crans.org/besson/teach/intro_num_DEM_2020/)
# - Date : mercredi 14/10/2020 et vendredi 16/10/2020.


# ----
# ## Factorielle $n \mapsto n!$
#
# Pour calculer les fonctions $\exp, \cos, \sin$, on peut avoir besoin de la factorielle, définie comme cela :
#
# $$ \texttt{factorielle}(n) = n! = 1 \times 2 \times \dots \times n, \; \text{si}\, n \geq 1$$
# et $\texttt{factorielle}(0) = 1$ si $n = 0$ (par convention).


def factorielle(n):
    """ Calcul naïf de la factorielle, avec des produits."""
    if n <= 0:  # si n <= 0 factorielle(n) = 1 par convention
        return 1
    else:       # sinon n > 0, on calcule avec des produits
        fact = 1
        i = 2
        while i <= n:
            # pour l'instant fact = 1 * 2 * ... * (i-1)
            fact = ...  # /!\ à vous d'écrire quelque chose ici
            # désormais      fact = 1 * 2 * ... * (i-1) * i
            i = i + 1
        # finalement fact = 1 * 2 * ... * n comme demandé
        return fact


# Par exemple on peut afficher les premières valeurs :


i = 0
while i <= 10:
    print("Factorielle de", i, "=", factorielle(i))
    i = i + 1


# Comme on l'observe ici, la factorielle est une fonction qui grandit *très très* vite !

# ----
# ## Exponentielle $x \mapsto \exp(x)$
#
# Une des définitions de la fonction exponentielle est la suivante :
#
# $$\exp(x) = \sum_{n=0}^{+\infty} \frac{x^n}{n!} = \lim_{N \to +\infty} \sum_{n=0}^{N} \frac{x^n}{n!}$$
#
# Vous n'avez normalement pas vu en cours de mathématiques la définition d'une somme infinie comme cela. L'essentiel est de croire que c'est bien définit, et de retenir que cette notation a un sens lorsque les termes successifs sont décroissants et tendent vers $0$ assez vite. (ça peut aussi avoir un sens dans d'autres cas, mais nous n'en parlons pas ici)
#
# C'est le cas ici avec le terme général $x^n / n!$ qui tend très vite vers $0$ (en effet la factorielle est une fonction qui grandit très très vite !).
#
# Et donc la valeur de la somme infinie est très bien approchée par la somme des quelques premiers termes, inutile d'aller trop loin !
#
# On va pouvoir calculer une approximation de $\exp(x)$ en calculant la somme des $N$ premiers termes, par exemple pour $N=30$ :
# $$\exp(x) \simeq \sum_{n=0}^{N=30} \frac{x^n}{n!} = \frac{x^0}{0!} + \frac{x^1}{1!} + \dots + \frac{x^{30}}{30!}$$
#
# Par exemple, pour $x=1$ on peut vérifier que les premiers termes convergent rapidement vers $\exp(1) = \mathrm{e} \simeq = 2.718281...$ :


x = 1
valeur_approchee_de_exp_1 = x**0/factorielle(0)
print(valeur_approchee_de_exp_1)
valeur_approchee_de_exp_1 += x**1/factorielle(1)
print(valeur_approchee_de_exp_1)
valeur_approchee_de_exp_1 += x**2/factorielle(2)
print(valeur_approchee_de_exp_1)
valeur_approchee_de_exp_1 += x**3/factorielle(3)
print(valeur_approchee_de_exp_1)
valeur_approchee_de_exp_1 += x**4/factorielle(4)
print(valeur_approchee_de_exp_1)
valeur_approchee_de_exp_1 += x**5/factorielle(5)
print(valeur_approchee_de_exp_1)
valeur_approchee_de_exp_1 += x**6/factorielle(6)
print(valeur_approchee_de_exp_1)
valeur_approchee_de_exp_1 += x**7/factorielle(7)
print(valeur_approchee_de_exp_1)
valeur_approchee_de_exp_1 += x**8/factorielle(8)
print(valeur_approchee_de_exp_1)
valeur_approchee_de_exp_1 += x**9/factorielle(9)
print(valeur_approchee_de_exp_1)
# Avec 9 termes, on a déjà les 6 premières décimales correctes ~= 2.718281


# ##### Premier exercice
#
# Compléter la fonction ci dessous, et testez la avec $x=1$.


def exp(x):
    """ Approximation de exp(x) avec sa série calculée aux N=30 premiers termes."""
    N = 30
    n = 1
    exp_x = 1.0
    while n < N:
        # pour l'instant exp_x = x**0/0! + x**1/1! + ... + x**(n-1)/(n-1)!
        exp_x = ...  # # /!\ à vous d'écrire quelque chose ici
        # désormais exp_x = x**0/0! + x**1/1! + ... + x**(n-1)/(n-1)! + x**n/n!
        n = n + 1
    return exp_x



print("Notre approximation de exp(1) =", exp(1))


# ##### Comparaison avec la fonction `math.exp`
#
# Dans le cours, je ne vous ai pas expliqué le concept de module et d'importation de modules.
#
# Sans rentrer dans tous les détails, voici à quoi ça sert :
#
# - quelqu'un (vous ou les développeurs de Python ou n'importe qui) a écrit du code Python qui réalise certaines fonctionnalités,
# - si vous souhaitez vous en servir, au lieu de tout réécrire dans votre fichier Python, vous pouvez stocker leur fichier dans le même dossier que votre fichier Python (ou ailleurs, par exemple dans un fichier accessible par Python dans son dossier d'installation),
# - et on peut demander à Python d'aller lire cet autre fichier, pour en **importer** les fonctionnalités.
#
# Par exemple, quand vous avez installez Python sur votre système, un fichier `math.py` a été installé quelque part où Python sait le lire, et on peut l'importer pour avoir accès à des constantes mathématiques ($\pi$) et des fonctions mathématiques ($\exp,\cos$ etc) déjà implémentée par les développeurs de Python.


import math
# on peut afficher le début de la documentation de ce module
print(math.__doc__)


# Par exemple, il y a la fonction `math.exp` qui calcule l'exponentielle :


print("D'après math.exp, exponentielle de 1 =", math.exp(1))


# Si vous souhaitez lire la documentation d'une fonction, on peut utiliser `help(fonction)` comme cela :
#
# Vous pouvez aussi aller regarder la documentation [en ligne](https://docs.python.org/3/library/math.html#math.exp) à l'adresse [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)


help(math.exp)


# Cela peut donc nous permettre de comparer votre implémentation avec celle du module `math` et de vérifier que le calcul approché de $\exp(x)$ que vous avez écrit est proche de celui de `math.exp` :


for i in range(1, 10):
    exp_i = exp(i)
    true_exp_i = math.exp(i)
    print("exp(", i, ") est calculé =", exp_i, "avec notre fonction, et =", true_exp_i, "avec math.exp")
    precision_relative = abs(exp_i - true_exp_i) / true_exp_i
    print("  soit une précision relative =", precision_relative)


# ##### Note sur les modules
# Python est fournit par défaut avec plein de modules réalisant des fonctionnalités diverses, comme lire des fichiers CSV ([`csv`](https://docs.python.org/3/library/csv.html)), calculer des statistiques sur des nombres ([`statistics`](https://docs.python.org/3/library/statistics.html), calculer des nombres aléatoires ([`random`](https://docs.python.org/3/library/random.html), envoyer des emails, télécharger des fichiers depuis Internet, et plein d'autres choses (voir [https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)).
#
# Par ailleurs, la communauté des utilisateurs et utilisatrices de Python est très active depuis 20 ans, et des milliers de modules (on dit aussi des paquets ou *packages*) existent.
# Les plus connus et les plus utilisés sont [`numpy`](https://www.numpy.org) pour calculer efficacement et facilement sur des tableaux de nombres, [`matplotlib`](https://www.matplotlib.org) pour dessiner des graphiques en 2D et en 3D (courbes scientifiques) et plein d'autres. Voir le site [https://pypi.org](https://pypi.org) (Python Package Index).
#
# Il existe aussi des packages conçus pour développer des applications web (Django), des jeux vidéos (PyGame, [et d'autres](https://analyticsindiamag.com/top-9-python-frameworks-for-game-development/)), lire et travailler avec des fichiers Excel, etc.

# ##### Bonus : une version plus efficace
#
# En étant observateur-trice des calculs effectués dans la fonction précédente, on remarque qu'à chaque étape on calcule $x^n$ et $n!$ entièrement.
# - Mais par définition, si on a la valeur de $x^(n-1)$ (calculée à l'étape $n-1$), calculer $x^n$ se fait comme $x^n = x^(n-1) * x$ plus efficacement qu'en recalculant entièrement $x^n$ (une seule multiplication contre une mise à la puissance).
# - De même, si on a la valeur de $(n-1)!$ (calculée à l'étape $n-1$), calculer $n!$ se fait comme $n! = (n-1)! * n$, plus efficacement qu'en recalculant entièrement $n!$.

# > ###### Note pour les curieux-ses :
# > On peut vérifier que le calcul direct de `x**n` est environ trois fois plus lent que le calcul de `y*x` si on a déjà `y=x**(n-1)` (105 ns contre 33 ns sur ma machine, avec par exemple `x = 2.9874` et `n = 40`.


def exp(x):
    """ Approximation de exp(x) avec sa série calculée aux N=30 premiers termes."""
    N = 50
    n = 1
    exp_x = 1.0
    # on stocke les calculs de x**n et n! dans deux variables
    x_puissance_n = x
    factoriel_n   = 1.0
    while n < N:
        exp_x = exp_x + (x_puissance_n / factoriel_n)
        n = n + 1
        # on met à jour efficacement ces deux variables
        x_puissance_n = x_puissance_n * x
        factoriel_n   = factoriel_n * n
    return exp_x


print("Vous devez remplir le fichier et faire l'exercice")
print("Fin du fichier squelette_exp.py")
