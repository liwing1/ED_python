a, t = [int(x) for x in input().split()]
lista = list()

for i in range(a):
    entrada = input().split()
    lista.append([entrada[0], " ".join(entrada[1:])])

lista.sort()
lista.reverse()

for i in range(t):
    n = int(input())
    print(lista[n-1][1], sep="", end=" (")
    print(lista[n-1][0], end=")\n")