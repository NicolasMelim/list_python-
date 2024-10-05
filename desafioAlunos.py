alunos_cursoA = {1, 2, 3, 4, 5, 6}
alunos_cursoB ={4, 5, 6, 7, 8}

intersecao = alunos_cursoA.intersection(alunos_cursoB)
print(f'Ambos alunos em: {intersecao}')

lista = [alunos_cursoA.difference(alunos_cursoB)]
print(f'Listando os diferentos alunos!: {lista}' )

lista2 = [alunos_cursoA.union(alunos_cursoB)]
print(f'Listandos ambos alunos dos dois cursos mas sem repetições: {lista2}')

dif_simetrica = alunos_cursoA.symmetric_difference(alunos_cursoB)
print(f'Alunos que estão em apenas um curso: {dif_simetrica}')