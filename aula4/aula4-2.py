salarioInicial = float(input('Insira o salário inicial: '))
aumento = float()
percentual = float()
salario = salarioInicial
salario2 = salarioInicial

for ano in range(2005,2023):
    if(ano == 2005):
        percentual = 0
    elif(ano == 2006):
        percentual = 1.5
    else:
        percentual = percentual * 2
    aumento = (percentual / salarioInicial) * 100.0
    aumento2 = (percentual / salario2) * 100.0
    salario += aumento
    salario2 += aumento2
    

print("O salário em 2023 é igual a R$ " + str(salario))
print("O salário em 2023 é igual a R$ " + str(salario2))
