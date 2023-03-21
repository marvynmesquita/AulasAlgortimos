numero = int(input("Digite um número: "))
fatorial = 0

for i in range(1, numero):
    fatorial += (numero - i)
    print(numero - i, fatorial)

print(f"O fatorial de {numero} é {fatorial}")