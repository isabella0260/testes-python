#empréstimo bancarios
valor_casa = (float(input("Quanto custa a casa que deseja comprar? ")))
salario = float(input("quanto você recebe de salário? "))
salario_minimo = salario * 30 / 100
anos = int(input("em quantos anos deseja pagar? "))
prestacao = valor_casa / (anos*12) 
if prestacao > salario_minimo:
    print("seu empréstimo foi negado", "a prestação seria de {:.2f}".format, (prestacao))
else:
    print("seu emprestimo foi aprovado, suas parcelas serão de:" "{:.2f}".format (prestacao), "em", anos, "anos")