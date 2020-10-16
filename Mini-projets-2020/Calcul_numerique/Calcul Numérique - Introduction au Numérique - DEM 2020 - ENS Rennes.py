#!/usr/bin/env python
# coding: utf-8

# # Dernier TP (mini projet) : exemples de calcul numérique
# 
# Le but de ce mini-projet est de vous faire implémenter manuellement des fonctions Python qui calculent des approximations des fonctions mathématiques suivantes :
# 
# $$ x \mapsto \sqrt{x} $$
# $$ x \mapsto \exp{x} $$
# $$ x \mapsto \cos{x} $$
# $$ x \mapsto \sin{x} $$
# 
# Pour chaque fonction, je vous donne dans ce document l'algorithme mathématique à appliquer, ainsi qu'un squelette à remplir.
# Vous pouvez télécharger les fichiers [squelette_sqrt.py](https://perso.crans.org/besson/teach/intro_num_DEM_2020/squelette_sqrt.py), [squelette_exp.py](https://perso.crans.org/besson/teach/intro_num_DEM_2020/squelette_exp.py), [squelette_cossin.py](https://perso.crans.org/besson/teach/intro_num_DEM_2020/squelette_cossin.py) sur le site du cours et le remplir.
# 
# Notez que les trois fonctions $\exp,\cos,\sin$ seront très proches, une fois que vous en avez fait une les autres se ressembleront beaucoup. Les deux dernières ($\cos$ et $\sin$) sont donc des bonus.
# 
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

# In[39]:


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
        
        # maintenant le calcul
        n = n + 1
        ...   # /!\ à vous d'écrire quelque chose ici
    return x_n


# ##### Exemples avec des valeurs entières

# In[46]:


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

# In[48]:


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

# In[49]:


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

# In[50]:


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


# ----
# ## Factorielle $n \mapsto n!$
# 
# Pour calculer les fonctions $\exp, \cos, \sin$, on peut avoir besoin de la factorielle, définie comme cela :
# 
# $$ \texttt{factorielle}(n) = n! = 1 \times 2 \times \dots \times n, \; \text{si}\, n \geq 1$$
# et $\texttt{factorielle}(0) = 1$ si $n = 0$ (par convention).

# In[61]:


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

# In[64]:


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

# In[92]:


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

# In[68]:


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


# In[93]:


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

# In[16]:


import math
# on peut afficher le début de la documentation de ce module
print(math.__doc__)


# Par exemple, il y a la fonction `math.exp` qui calcule l'exponentielle :

# In[17]:


print("D'après math.exp, exponentielle de 1 =", math.exp(1))


# Si vous souhaitez lire la documentation d'une fonction, on peut utiliser `help(fonction)` comme cela :
# 
# Vous pouvez aussi aller regarder la documentation [en ligne](https://docs.python.org/3/library/math.html#math.exp) à l'adresse [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

# In[10]:


help(math.exp)


# Cela peut donc nous permettre de comparer votre implémentation avec celle du module `math` et de vérifier que le calcul approché de $\exp(x)$ que vous avez écrit est proche de celui de `math.exp` :

# In[60]:


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

# In[69]:


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

# In[71]:


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


# In[81]:


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

# In[71]:


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


# In[80]:


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


# ## Conclusion
# 
# J'espère que cette activité vous aura plu.
