import math
valores = input().split()

a, b, c = float(valores[0]), float(valores[1]), float(valores[2])

delta = (b ** 2) -4 * a * c 

if a == 0 :
    print("Impossivel calcular")
    
elif delta < 0:
    print("Impossivel calcular")
else: 
    r1 = (-b + math.sqrt(delta)) / (2 * a )
    r2 = (-b - math.sqrt(delta)) / (2 * a )
    
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")