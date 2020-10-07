#!/usr/bin/env python
# -*- encoding: utf8 -*-
"""
Test de désasemblage sur le code suivant :
    x = 3
    y = 20
    print(x + y)
"""

code = "x = 3; y = 20; print(x + y)"
print("Pour le code suivant :")
print(code)

print("Si on l'exécute :")
exec(code)

import dis
print("dis.dis(code) donne le bytecode (représentation intermédiaire) suivant :")
dis.dis(code)
