n = int(input())
maior = None
menor = None
#soma = 0   qual o problema de botar a soma aqui??


for _ in range (n):

    x, y = input().split()
    x, y = int(x), int(y)

    soma = 0
    if x % 2 == 0:
        x = x + 1
        for i in range (y):
            soma = soma + x
            x = x + 2
        print(soma)

    else:
        for i in range (y):
            soma = soma + x
            x = x + 2
        print(soma)


    if maior == None or soma > maior:
        maior = soma
        
    if menor == None or soma < menor:
        menor = soma

    media = (maior + menor)/2

print(maior)
print(menor)
print('{:.2f}'.format(media))