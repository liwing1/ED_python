class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0,item)

    def addRear(self, item):
        self.items.append(item)
        
    def addIndex(self, item, index):
        self.items.insert(index, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop(len(self.items)-1)
    
    def removeIndex(self, index):
        return self.items.pop(index)
    
    def size(self):
        return len(self.items)
    
d = Deque()

entrada = [0, 0, 0]
tempo = 0

while True:
    
    entrada = input().split()
    
    if entrada[0] == "i":
        if entrada[2] == "0":
            d.addRear([entrada[1], tempo])
        else:
            d.addRear([entrada[1], tempo, str(d.size()-int(entrada[2]))])
        
    elif entrada[0] == "r":
        cont = 0
        i=0
        while i < (len(d.items)-cont):
            if entrada[1] == d.items[i][0]:
                for j in range(i, len(d.items)):
                    if len(d.items[j]) > 2:
                        if d.items[j][2] == str(i):
                            d.items[j] = [d.items[j][0],d.items[j][1]]
                            
                        elif int(d.items[j][2]) > i:
                            d.items[j] = [d.items[j][0], d.items[j][1] , str(int(d.items[j][2])- 1)]
                d.removeIndex(i)
                cont += 1
            i += 1
    
    elif entrada[0] == "f":
        if d.isEmpty():
            print(-1)
        else:
            for i in range(len(d.items)):
                for j in range(len(d.items[i])):
                    d.items[i][j] = int(d.items[i][j])
            for i in d.items:
                print(str(i).replace(" ",""), end = " ")
        break
    
    tempo += 1
