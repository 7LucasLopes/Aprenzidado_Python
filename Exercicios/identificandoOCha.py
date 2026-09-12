t = int(input())

r = input().split()
respostas = []

for i in r:
    respostas.append(int(i)) 

contador = 0
for i in respostas:

    if i == t:
        contador+= 1
print(contador)