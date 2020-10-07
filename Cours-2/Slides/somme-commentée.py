#
# Ce petit programme calcule la somme des n premiers entiers
# n est le nombre d'entiers qu'on veut additionner
#
n = 5
sauven = n
# s va contenir la somme
s = 0
# Boucle de calcul
while n > 0:
  print("J'en suis à n = ", n)
  # accumuler n dans s
  s = s + n
  print("S vaut maintenant: ",s)
  # Décrémenter n
  n = n - 1
# À la fin, on affiche la valeur de s
print( "La somme des ", sauven, " premiers entiers est: ", s )
