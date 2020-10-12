# -*- coding: utf-8 -*-
#
# Cette fonction donne le rang du plus grand
# element de la liste x. Il faut faire attention que les
# nombres peuvent etre negatifs
#
def numéroPlusGrande(tas):
  """
  numéroPlusGrand(tas) donne l'indice dans la liste d'entiers tas
  du plus grand élément. Si la liste est vide, le résultat est -1 par
  convention. On suppose les entiers positifs ou nuls.
  """
  # Si le tas est vide, on rend la valeur -1
  if tas == []:
    return(-1)
  # On trouve l'élément maximum
  maxCrêpe = max(tas)
  # tas.index(v) donne le numéro de l'element de tas qui a la valeur v
  indexMax = tas.index(maxCrêpe)
  return(indexMax)

def testNuméroPlusGrande():
  print('numéroPlusGrande([1,6,7,3,2]) == 2): ',numéroPlusGrande([1,6,7,3,2]) == 2)
  print('numéroPlusGrande([]) == 0: ', numéroPlusGrande([]) == -1)
  return 0

#
# Cette fonction retourne les elements de x, a partir
# de numéro. Retourner veut dire, inverser les elements
#
def retournerTas(x,numéro):
  """
  retournerTas(x,numéro) retourne la partie du tas x qui commence à 
  l'indice numéro
  """
  tasDuBas = x[:numéro]
  tasDuHaut = x[numéro:]
  tasDuHaut.reverse()
  result = tasDuBas + tasDuHaut
# print(result)
  return result

def testRetournerTas():
  """
  test de retournerTas
  """
  print('retournerTas([1,2,3,4,5],2): ', retournerTas([1,2,3,4,5],2) )
  print('retournerTas([],1): ', retournerTas([],1) )
  print('retournerTas([1,2,3],0): ', retournerTas([1,2,3],0))
  return 0


#
# Ceci est le programme principal
#
def main():
  """
  Ce programme permet d'effectuer des tests
  """
  testNuméroPlusGrande()
  testRetournerTas()
 
if __name__ == '__main__': main()


