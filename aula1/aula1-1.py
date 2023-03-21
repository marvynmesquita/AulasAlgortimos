numeros = []
i = 0
j = 0
soma = float(0)
while i < 3:
    numeros.append(float(input("Digite um número: ")))
    i += 1


while j < len(numeros):
    soma += float(numeros[j])
    j += 1

media = soma / len(numeros)

print(f"A média dos números digitados é {media}")
    