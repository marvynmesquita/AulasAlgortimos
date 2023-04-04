n = int(input("Digite o numero máximo de termos a ser calculado: "))
a = 1
print(a)
for i in range(n+1):
    if a == 1:
        print(a)
        b = a
        a += 1
    else:
        a = a + b
        b = a - b
        print(a)
