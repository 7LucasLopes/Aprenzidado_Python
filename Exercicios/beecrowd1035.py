valor = input().split()

a, b, c, d = int(valor[0]), int(valor[1]), int(valor[2]), int(valor[3])

somaAB = a + b
somaCD = c + d

if b > c and d > a and somaCD > somaAB and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores ao aceitos")