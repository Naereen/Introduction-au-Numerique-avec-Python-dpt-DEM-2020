#!/usr/bin/env python
# coding: utf-8

# Dernier TP (mini projet) : exemples de calcul numérique
# - Prof : Lilian Besson
# - Site du cours : [https://perso.crans.org/besson/teach/intro_num_DEM_2020/](https://perso.crans.org/besson/teach/intro_num_DEM_2020/)
# - Date : mercredi 14/10/2020 et vendredi 16/10/2020.

# ----
# ## Cosinus et sinus (bonus)

# ### Cosinus
# Une des définitions de la fonction cosinus est la suivante :
#
# $$\cos(x) = \sum_{n=0}^{+\infty} \frac{(-1)^n * x^{2n}}{(2n)!}$$
#
# On va pouvoir calculer une approximation de $\cos(x)$ en calculant la somme des $N$ premiers termes, par exemple pour $N=30$ :
# $$\cos(x) \simeq \sum_{n=0}^{N=30} \frac{(-1)^n x^{2n}}{(2n)!} = \frac{x^0}{0!} - \frac{x^2}{2!} + \dots - \frac{x^{2*29}}{(2*29)!} + \frac{x^{2*30}}{(2*30)!}$$
#
#
# - Question : en vous inspirant de votre code pour `exp(x)`, écrire une fonction `cos(x)`.
# - Sur quelques valeurs que vous connaissez peut-être ($x=0, \pi/4, \pi/2$), comparez la avec la fonction `math.sin` (ou avec celle de votre calculatrice).


def cos(x):
    """ Approximation de cos(x) avec sa série calculée aux N=30 premiers termes."""
    N = 30
    n = 1
    cos_x = 1.0
    while n < N:
        # pour l'instant cos_x = x**0/0! - x**1/1! +
        #  ... + (-1)**(n-1) x**(2*(n-1))/(2*(n-1))!
        cos_x = ...  # # /!\ à vous d'écrire quelque chose ici
        # désormais cos_x = x**0/0! - x**1/1! + ...
        #  ... + (-1)**(n-1) x**(2*(n-1))/(2*(n-1))! + (-1)**n x**(2*n)/(2*n)!
        n = n + 1
    return cos_x



x = 0
print("Pour x = 0, cos(x) =", cos(x))     # expected: 1
x = math.pi / 4
print("Pour x = pi/4, cos(x) =", cos(x))  # expected: sqrt(2)
x = math.pi / 2
print("Pour x = pi/2, cos(x) =", cos(x))  # expected: 0

x = 10*2*math.pi
print("Pour x = 10*2*pi, cos(x) =", cos(x))     # expected: 1
x = 10*2*math.pi + math.pi / 4
print("Pour x = 10*2*pi + pi/4, cos(x) =", cos(x))  # expected: sqrt(2)
x = 10*2*math.pi + math.pi / 2
print("Pour x = 10*2*pi + pi/2, cos(x) =", cos(x))  # expected: 0


# Commentez sur la perte de précision observée entre les deux calculs de $\cos(\pi/2)$ et $\cos(10*2*\pi + \pi/2)$ alors que leurs valeurs exactes (mathématiques) sont égales.

# ### Sinus
# Pour la fonction sinus, la définition est très similaire :
#
# $$\sin(x) = \sum_{n=0}^{+\infty} \frac{(-1)^n * x^{2n+1}}{(2n+1)!}$$
#
# - Question : en vous inspirant de votre code pour `exp(x)` et `cos(x)`, écrire une fonction `sin(x)`.
# - Sur quelques valeurs que vous connaissez peut-être ($x=0, \pi/4, \pi/2$), comparez la avec la fonction `math.sin` (ou avec celle de votre calculatrice).


def sin(x):
    """ Approximation de sin(x) avec sa série calculée aux N=30 premiers termes."""
    N = 30
    n = 1
    sin_x = 1.0
    while n < N:
        # pour l'instant sin_x = x*1/1! - x*3/3! + ...
        #  ... + (-1)*(n-1) x*(2*(n-1)+1)/(2*(n-1)+1)!
        sin_x = ...  # # /!\ à vous d'écrire quelque chose ici
        # désormais sin_x = x*1/1! - x*3/3! + ...
        #  ... + (-1)*(n-1) x*(2*(n-1)+1)/(2*(n-1)+1)! + (-1)*n x*(2*n+1)/(2*n+1)!
        n = n + 1
    return sin_x



x = 0
print("Pour x = 0, sin(x) =", sin(x))     # expected: 0
x = math.pi / 4
print("Pour x = pi/4, sin(x) =", sin(x))  # expected: sqrt(2)
x = math.pi / 2
print("Pour x = pi/2, sin(x) =", sin(x))  # expected: 1

x = 10*2*math.pi
print("Pour x = 10*2*pi, sin(x) =", sin(x))     # expected: 0
x = 10*2*math.pi + math.pi / 4
print("Pour x = 10*2*pi + pi/4, sin(x) =", sin(x))  # expected: sqrt(2)
x = 10*2*math.pi + math.pi / 2
print("Pour x = 10*2*pi + pi/2, sin(x) =", sin(x))  # expected: 1


print("Vous devez remplir le fichier et faire l'exercice")
print("Fin du fichier squelette_cossin.py")


# ## Conclusion
#
# J'espère que cette activité vous aura plu.
