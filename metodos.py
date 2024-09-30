extend = ["Nicolas", "Nike", "Vans"]
extend.extend(["AOC", "Razer"])
print(extend) #Com o append, vc precisa colcoar de 1 em 1. Com o extend voce pode colocar uma lista dentro de outra ja: exemplo APPEND ABXIDO

ap =["Nicolas", "Nike", "Vans"]
ap.append("AOC")
ap.append("Razer")
print(ap) #LISTA DENTRO DE OUTRA LISTA.



pol = ["Carro", "Computador", "Mouse"]
print(pol)
pol.pop(0) #remove atraves do index
print(pol)


rem = ["Casa", "Teclado", "MOUSE PAD", "Maze"]
rem.remove("MOUSE PAD")  #REMOVE ESCREVENDO O OBJETO.
print(rem)

sor = ["Python", "JavScript", "java", "C++"]
print(sorted(sor)) #ORDEM ALFABETICA 

sorte = ["J", "K ", "A", "V", "L"]
sorte.sort()
print(sorte)
 
 
x = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 