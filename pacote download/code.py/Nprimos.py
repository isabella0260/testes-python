num = int(input("digite um número: "))
total = 0
for c in range (1, num+1):
    if num % c == 0:
        total=total+1
print (f'o numero {num} foi dividido {total} vezes')
if total == 2:
    print(num, 'é um número primo')
else:
    print(num, 'não é um número primo')