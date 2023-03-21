numeros = []
media = 0
for i in range(0,5):
    numeros.append(float(input('Digite um número: ')))

for a in range(len(numeros)):
    media += numeros[a]

media = media / len(numeros)
print('A média dos números digitados é {}'.format(media))