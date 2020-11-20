def time_vectorize( arg_input ):
    arg_vec = []
    arg_vec.append(int(arg_input.split()[0]))
    for i in arg_input.split()[1].split(":"):
        arg_vec.append(int(i))
    return arg_vec

def duracao(ini, fim):
    tempo_total = 0
    for i in range(len(ini)):
        tempo = fim[i]-ini[i]
        if i == 0:
            tempo_total += tempo*24*60*60
        elif i == 1:
            tempo_total += tempo*60*60
        elif i == 2:
            tempo_total += tempo*60            
        else:
            tempo_total += tempo
    return tempo_total
    
ini_vec = time_vectorize(input())
fim_vec = time_vectorize(input())

tempo_total = duracao(ini_vec, fim_vec)

if tempo_total>0:
    dias = tempo_total // (24*60*60)
    tempo_total -= dias * (24*60*60)
    print(f"{dias} dia(s)")

    horas = tempo_total // (60*60)
    tempo_total -= horas * (60*60)
    print(f"{horas} hora(s)")

    minutos = tempo_total // (60)
    tempo_total -= minutos * (60)
    print(f"{minutos} minuto(s)")

    segundos = tempo_total
    tempo_total -= segundos
    print(f"{segundos} segundo(s)")
else:
    print("Data inválida!")