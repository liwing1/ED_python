tam_arq = int(input())
print("Transmitindo {} bytes...".format(tam_arq))
ult_5 = 0
tx_vec = []
contador = 0
while ult_5 - tam_arq < 0:
    tx = int(input())
    ult_5 = ult_5 + tx
    tx_vec.append(tx)
    contador = contador + 1
    if (contador % 5) == 0:
        arq_left = tam_arq - ult_5
        tx_media = sum(tx_vec) / 5
        if ult_5 >= tam_arq:
            break
        elif tx_media == 0:
            print("Tempo restante: pendente...")
        else:
            if (arq_left/tx_media) - int(arq_left/tx_media) > 0:
                temp = int(arq_left / tx_media) + 1
            else:
                temp = int(arq_left/tx_media)
            print("Tempo restante: {} segundos.". format(temp))
        tx_vec.clear()

print(f"Tempo total: {contador} segundos.")