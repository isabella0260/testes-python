ano_nasc = int(input("Qual ano você nasceu? "))
ano_atual = int(input("Qual ano nós estamos? "))
idade = (ano_atual - ano_nasc)
if idade > 18:
    print("você tem: ", idade, "anos. Você já é maior de idade")
else: 
    print("você tem: ", idade, "anos. Você ainda é menor de idade")