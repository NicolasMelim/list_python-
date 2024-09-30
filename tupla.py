#não podemos modificar uma tupla, como ja sabiamos. 
#é bom começar a criar uma tupla com uma virgula no final 
#para acessar o index uma tupla é igual na lista [1] e assim vai... 


tui = ("Oi", "Tudo", "Bem",)

for i in tui:
    print(i)



tupla = (1, 2, 3, 4, 5 ,6 ,8 ,)

print(tupla[1])

print(tupla[3])

print(tupla[5])



carros = ("gol")
print(isinstance(carros, tuple))