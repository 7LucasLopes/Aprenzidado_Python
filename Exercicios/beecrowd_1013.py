a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a + b + abs(a - b)) // 2

maiorFinal = (maiorAB + c + abs(maiorAB - c)) // 2

print(f"{maiorFinal} eh o maior")