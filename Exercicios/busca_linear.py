"""Apredizado sobre tempo de execução!"""



Esse possui um tempo de execução Linear O(n). Nesse exercício meu programa precisou rodar 8 vezes até encontrar a resposta.

alunos = ["Lucas", "Sophia", "Nikely", "Adelaide", "Cristovão", "Walterson", "Gabriel", "Beatriz", "Thiago"]
procurado = "Beatriz"

for i in range(len(alunos)):

    if alunos[i] == procurado:
        print(f"Achei o nome {procurado} no índice {i}")


numeros = [45, 50, 89, 150, 1024, 1, 0 , -56, 75, 63, 7989]
maior = numeros[0]
for i in numeros:
    if i > maior:
        maior = i

print(f"Maior número da lista: {maior}")
    
