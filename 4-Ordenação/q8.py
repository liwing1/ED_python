n = int(input())
lista = []

def print_tempo(Voltas):
    minutos = round(Voltas // 60)
    segundos = int((Voltas - minutos*60))
    milli = round(Voltas - (minutos*60) - segundos, 3)
    
    return str(minutos) + ":" + str(segundos).zfill(2) + "." + str(int(milli*1000)).zfill(3)

for i in range(n):
    Nome = input()
    Voltas = sum([float(x) for x in input().split()])
    lista.append([Voltas]+ [Nome])
    
lista = (sorted(lista))

for i in range(n):
    print(f"{i+1}. {lista[i][1]} ({print_tempo(lista[i][0])})")