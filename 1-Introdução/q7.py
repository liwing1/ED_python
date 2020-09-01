n=0
tam_arq = int(input())

print(f"Transmitindo {tam_arq} bytes...")

print(round(3.3333))

while tam_arq:
    taxa = int(input())
    restante = tam_arq - taxa
    n += 1
    if n % 5:
        round((tam_arq - restante)/5)
