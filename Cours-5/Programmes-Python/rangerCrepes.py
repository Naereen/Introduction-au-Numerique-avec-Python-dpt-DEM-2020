# -*- coding: utf-8 -*-
from fonctions import numéroPlusGrande
from fonctions import retournerTas

def rangerCrêpes( tas ):
  """
  rangerCrêpes(tas) range la liste d'entiers positifs qui représente
  un tas de crêpes.
  """
  print("\n *** Je vais ranger le tas: ", tas)

  # D'abord, si le tas est vide, on le rend tel qu'il est car 
  # il est rangé
  if tas == []:
    print("Sur un tas vide, il n'y a rien à faire")
    return( tas )

  # On cherche le numéro de la plus grande crepe
  plusGrandeCrêpe = numéroPlusGrande( tas )
  print("La plus grande crêpe est la crêpe numéro : ", plusGrandeCrêpe)

  # Si le numéro de la plus grande crêpe est 0, 
  # on range la pile qui se trouve juste au dessus
  if plusGrandeCrêpe == 0:
    print("La première crêpe est déjà rangée. Je m'attaque à la pile: ", tas[1:])
    return( tas[:1]+rangerCrêpes(tas[1:]) )

  # Si ce n'est pas le cas, on retourne le tas à partir
  # de la plus grande crêpe
  tasRetourné = retournerTas(tas,plusGrandeCrêpe)
  print('Je retourne le tas à partir de la plus grande crêpe: ', tasRetourné)

  # Puis on retourne tout
  tasRetourné = retournerTas(tasRetourné,0)
  print("Je retourne tout: ", tasRetourné)
  return(tasRetourné[:1]+rangerCrêpes(tasRetourné[1:]))

def testRangerCrêpes():
  """
  Test de le fonction rangerCrêpes
  """
  print( '\n ----- Premier test : rangerCrêpes([])\n')
  test1 = rangerCrêpes([])
  print( 'Résultat: ', test1)
  print( '\n ----- Second test: rangerCrêpes([1,3,2,5,4])\n')
  test2 = rangerCrêpes([1,3,2,5,4])
  print( 'Résultat: ', test2)
  return 0

#
# Ceci est le programme principal
#
def main():
  """
  Ce programme permet d'effectuer des tests
  """
  testRangerCrêpes()

if __name__ == '__main__': main()


