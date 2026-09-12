valor = float(input())

centavos = int(valor * 100)


notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]



print("NOTAS:")
    
for i in notas:
    
    divisor = centavos // i
    resto = centavos % i
    
    print(f"{divisor:.0f} nota(s) de R$ {i / 100:.2f}")
    centavos = resto

print("MOEDAS:")
for i in moedas:
    
    divisor = centavos // i
    resto = centavos % i
    
    print(f"{divisor:.0f} moeda(s) de R$ {i / 100:.2f}")
    centavos = resto