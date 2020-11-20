from operator import itemgetter, attrgetter


lista = list()

while(1):
    entrada = int(input())
    if entrada == 0:
        break
    
    for i in range(entrada):
        constante = input().split(" = ")
        
        
        lista.append([float(constante[1])-int(float(constante[1]))] + [constante[0]])
        
    lista = sorted(lista)
    
    for i in range(len(lista)):
        if i < len(lista)-1:
            print(lista[i][1], end=" < ")
        else:
            print(lista[i][1])
    lista = []