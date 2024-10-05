list = set([1, 2, 3 ,3, 4, 5])
print(list)

#set remove os duplicados.


lis2 ={1 ,2, 3}
lis3 = {4, 5, 6}
result = lis3.union(lis2)
print(result) # union ele une os dados em um SET só.


lis5 ={1 ,2, 3}
lis6 = {1, 2, 4}
resulta = lis6.difference(lis5) # ele pega o unico dado diferente de lista 6 com lista 4]
#ou seja o 4, pois ele nao aparece na lista 5!!!!
print(resulta)



set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


# Interseção: elementos presentes em ambos os conjuntos
intersecao = set1.intersection(set2)
print("Interseção:", intersecao)

# Diferença: elementos presentes em set1 e não em set2
diferenca = set1.difference(set2)
print("Diferença (set1 - set2):", diferenca)

# Diferença simétrica: elementos presentes em um ou outro conjunto, mas não em ambos
dif_simetrica = set1.symmetric_difference(set2)# ou seja, remove os itens que tem nos dois conjuntos!!
print("Diferença Simétrica:", dif_simetrica)