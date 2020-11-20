class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
n = None
anilha = None
soma = int()
cont = int()

while( n != 0):
    n = int(input())
    if n == 0:
        break
    s.push(n)
    
ret = int(input())

while ( anilha != ret ):
    if (not s.isEmpty()):
        anilha = s.pop()
    else:
        break
    print("Peso retirado:", anilha)
    soma += anilha
    cont += 1
    
print("Anilhas retiradas:", cont)
print("Peso total movimentado:", soma)
