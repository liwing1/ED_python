from operator import itemgetter, attrgetter
from random import randint

class Student:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return repr([self.nota, self.nome])


a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
S, i = min((abs(x - a) + (x - b) ** 2 + abs(x - c) ** 3 + (x - d) ** 4, x) for x in range(1, 124))
print(i)