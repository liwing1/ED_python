from operator import itemgetter, attrgetter
from random import randint
def listador():
    z, amount = input().split(' = ')
    if '.' in amount:
        x, y = map(int, amount.split('.'))
    else:
        x, y = int(amount), 0
    return (y, -x, z)

class Student:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return repr([self.nota, self.nome])

while(1):
    rep = int(input())
    if rep == 0:
        break
    else:
        constantes = [listador() for _ in range(rep)]
        print(' < '.join(j[2] for j in sorted(constantes)))