def somme_liste( l ):
  """
  somme_liste(l) donne la somme de tous les éléments de la liste d'entiers l
  """
  i = 0
  somme = 0
  while i<len(l):
    somme = somme + l[i]
    i=i+1
  print('La somme des éléments de la liste ', l, ' est: ', somme)
  
