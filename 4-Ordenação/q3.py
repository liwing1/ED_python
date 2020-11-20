lista = list()
for i in range(int(input())):
    lista.append(float(input()))
lista.sort()
lista.reverse()
for i in lista:
    print("{:.2f}".format(i))
