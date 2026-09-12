valor = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for i in range(len(cedulas)):

    divisor = valor // cedulas[i]
    resto = valor % cedulas[i]

    
    print(f"{divisor} nota(s) de R$ {cedulas[i]},00")
    valor = resto