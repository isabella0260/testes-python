from random import randint
computador = randint (0,5)
numero = (int(input("advinhe o número que eu pensei de 0 a 5: ")))
if numero == computador:
    print("parabéns você acertou!") 
else:
    print("você errou tente de novo")