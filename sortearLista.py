import random

name = ["Nicolas", "Augusto", "Alaor", "Goulart", "Doka", "Paulo"]
random.shuffle(name)
for i, indice in enumerate(name, start=1):
    print(i, indice)

    if i == 3:
        print("_" *10)



paises = ["Brasil", "Mexico", "Africa"]
x = 0
for i in paises:
    x += 1
    print(x, i)
 