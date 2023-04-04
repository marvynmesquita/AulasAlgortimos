o = int(input('Insira a quantidade de termos: '))
h = 0
for i in range(1,o+1):
    h += (1/i)
print('O valor de H é: ' + str(h))