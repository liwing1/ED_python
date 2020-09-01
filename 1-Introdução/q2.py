def max3(n1, n2, n3):
    vetor = [n1, n2, n3]
    maior = vetor[0]
    for elemento in vetor:
        if elemento > maior:
            maior = elemento
    return maior


print(max3(3.5, 1.666, 1000))
