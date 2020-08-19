n = int(input())
tupla = ()
saida = ""

for i in range(n):
    problema, solucao, dificuldade = input().split()
    dificuldade = int(dificuldade)
    tupla = tupla + (solucao, dificuldade)


for j in range(10, -1, -1):
    for k in range(len(tupla)):
        if tupla[k] == j:
            saida += tupla[k-1]
    print(j)
print(saida)
