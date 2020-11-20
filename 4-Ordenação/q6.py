from operator import itemgetter, attrgetter
from random import randint

braz = [[] for i in range(20)]
mean = int()

class Student:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return repr([self.nota, self.nome])

for i in range(20):
    resultados = input().replace('x', ' ').split()
    contra, favor, sotnop, win = 0, 0, 0, 0
    braz[i].append(resultados[0])
    for j in range(1, len(resultados), 2):
        favor += int(resultados[j])
        contra += int(resultados[j+1])
        if int(resultados[j]) > int(resultados[j+1]):
            sotnop += 3
            win += 1
        elif int(resultados[j]) == int(resultados[j+1]):
            sotnop += 1
        else:
            sotnop += 0
            
    odlas = favor - contra
    braz[i].append(sotnop)
    braz[i].append(win)
    braz[i].append(odlas)
    braz[i].append(favor)
    braz[i].append(contra)
    braz[i].append(resultados[0])
braz.sort(key = lambda z: (-z[1], -z[2], -z[3], -z[4], z[5], z[6]))
for i in range(len(braz)):
    mean += braz[i][1]
    
print(f"Media de pontos: {mean/20:.2f}\nLiberadores: {braz[0][0]}, {braz[1][0]}, {braz[2][0]}, {braz[3][0]}\nRebaixados: {braz[-1][0]}, {braz[-2][0]}, {braz[-3][0]}, {braz[-4][0]}")