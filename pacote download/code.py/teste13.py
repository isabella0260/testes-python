ano_nasc = int(input("digite seu ano de nascimento: "))
ano_atual = 2024
idade = 2024 - ano_nasc
if idade >= 18:
    print("já está na hora de se alistar")
elif idade > 25:
    print("já passou o tempo de se alistar, você está ", idade - 25, "anos atrasado")
elif idade < 18:
    print ("ainda não está na hora de se alistar, faltam ", 18 - idade, "anos")