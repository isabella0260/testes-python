emprestimo = float(input("Qual valor você precisa: "))
juros = ((emprestimo * 20)/100)
valor_total = float(emprestimo + juros)
print("você irá pagar: ", "{:.2f}".format (valor_total))
parcelas = int(input("em quantas vezes você quer dividir?"))
valor_parcela = (valor_total/parcelas)
print("suas parcelas serão de R$ ", valor_parcela, "em", parcelas, "vezes")