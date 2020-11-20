from operator import itemgetter, attrgetter
def menc(mencao):
    if mencao == "SS":
        return 5
    elif mencao == "MS":
        return 4
    elif mencao == "MM":
        return 3
    elif mencao == "MI":
        return 2
    elif mencao == "II":
        return 1
    elif mencao == "SR":
        return 0
    
def cnem(mencao):
    if mencao == 5:
        return 'SS'
    elif mencao == 4:
        return "MS"
    elif mencao == 3:
        return "MM"
    elif mencao == 2:
        return "MI"
    elif mencao == 1:
        return "II"
    elif mencao == 0:
        return "SR"

class Student:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return repr([self.nota, self.nome])
    

n = int(input())
lista = list()

for i in range(n):
    entrada = input().split()
    lista.append([" ".join(entrada[1:])] + [menc(entrada[0])])
    
lista = sorted(lista, reverse = False)
lista = sorted(lista, reverse = True, key = itemgetter(1))

for i in lista:
    print(cnem(i[1]), end=" ")
    print(i[0])
    