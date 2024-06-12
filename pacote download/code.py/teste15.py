contagem = 0 
soma = 0
maior = 0
menor = 0 
while contagem < 5:
    numero = int(input("digite os números: ")) 
    if numero > maior:
        maior = numero
    soma = soma + numero
    contagem = contagem + 1 
print ( "a soma de todos os valores é igual a: ", soma, "e o maior número é: ", maior, "o menor numero é: ", menor)
