numero = int(input("Digite um número: "))
for i in range(2, numero):
    if numero % i == 0:
        print(str(numero) + " não é primo")
        break
else:
    print(str(numero) + " é primo")