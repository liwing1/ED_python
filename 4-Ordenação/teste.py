def hparamin(horario):
    hora, minuto = [int(x) for x in horario.split(":")]
    return hora*60 + minuto

n = int(input())
agenda = list()
feitos = list()

for i in range(n):
    entrada = input().split()
    entrada.reverse()
    D, C, T = entrada[0], entrada[1], (entrada[2:].reverse())

    D = hparamin(D)
    C = hparamin(C)
    
    agenda.append([T, C, D])

for i in range(1, len(agenda)):
    if agenda[i][1] >= agenda[i-1][2] :
        cont += 1
        feitos.append(agenda[i])
    
        
