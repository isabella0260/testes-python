peso = float(input("digite quanto você pesa: "))
altura = float(input("digite qual é a sua altura: "))
imc = peso / (altura**2)
if imc >=18 and imc <25:
    print("seu imc é: " "{:.2f}".format (imc), "você está saudável")
else:
    print("seu imc é: " "{:.2f}".format (imc), "você não está saudável")