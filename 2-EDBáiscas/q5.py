class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

q = Queue()


entrada = input().split()

for i in range(len(entrada)):
    if i == len(entrada)-1:
        avancos = int(entrada[i])

    elif i < len(entrada)-1:
        q.enqueue(entrada[i])
        
for i in range(avancos):
    q.enqueue(q.dequeue())
    
for i in range(q.size()):
    if i == 0:
        pessoa_fim = q.items[i]
    if i == q.size()-1:
        pessoa_frente = q.items[i]
        
print("Pessoa da frente:", pessoa_frente)
print("Pessoa do fim:", pessoa_fim)