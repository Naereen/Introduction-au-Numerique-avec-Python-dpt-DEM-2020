phrase = input("Tape une (petite) phrase :")
i = 0
nombre_de_e = 0
while i < len(phrase):
    if phrase[i] == 'e':
        nombre_de_e = nombre_de_e + 1
    i = i+1
print("Le nombre de e dans ta phrase est :", nombre_de_e)

