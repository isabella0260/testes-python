#contagem progressiva e contagem regressiva:
v1 = int(input("digite o número que começa a contagem: "))
v2 = int(input("digite até quanto quer contar: "))
while v1 < v2: 
    if v1<v2:
        v1 = v1 + 1
        print (v1)
    else:
        v1 = v1 - 1
        print (v1)