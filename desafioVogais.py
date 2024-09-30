palavras = ["Python", "desafio", "Lista", "Palavra"]
vogais = "aeiouAEIOU"


for v in palavras:
    contagem_vogal = 0
    
    for letra in v:
        if letra in vogais:
            contagem_vogal += 1 
  
    if contagem_vogal == 1:
        print(f'A palavra "{v}" tem {contagem_vogal} vogal.')
    else:
        print(f'A palavra "{v}" tem {contagem_vogal} vogais.')