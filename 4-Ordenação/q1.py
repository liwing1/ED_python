contador = int()
n = int(input())
lista = input().split()
lista_rep = list()

for i in lista:
    if i not in lista_rep:
        lista_rep.append(i)
        contador += lista.count(i) - 1
        
print(contador)