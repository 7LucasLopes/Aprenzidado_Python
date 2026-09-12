valor = int(input())

hora = valor // 3600
resto = valor % 3600

minuto = resto // 60

segundo =  resto % 60

print(f"{hora}:{minuto}:{segundo}")