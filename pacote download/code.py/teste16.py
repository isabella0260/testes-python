#converter moedas 4 vezes
contagem = 0
conversor = int(input("quantas vezes você quer converter?"))
while contagem < conversor:
    real = float(input("quantos reais você tem?"))
    dolar = real / 5.10
    print("o valor R$","{:.2f}".format (real), "são US$", "{:.2f}".format(dolar))
    contagem = contagem + 1