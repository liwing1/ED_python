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
cont = 0

entrada = [0,0]
while entrada[0] != "X":
    entrada = input().split()

    if entrada[0] == "I":
        d.addFront(entrada[1])
        
    elif entrada[0] == "F":
        d.addRear(entrada[1])
    
    elif entrada[0] == "P":
        print(d.removeRear())
        
    elif entrada[0] == "D":
        print(d.removeFront())
    
    elif entrada[0] == "E":
        print(d.removeIndex(int(entrada[1])-1))
            
    elif entrada[0] == "T":
        for i in range(len(d.items)):
            if d.items[i] == entrada [1]:
                d.removeIndex(i)
                d.addIndex(entrada[2], i)
                break
        
    elif entrada[0] == "V":
        cont = 0
        for i in range(len(d.items)):
            if d.items[i-cont] == entrada[1]:
                d.removeIndex(i-cont)
                cont += 1
        print(cont)
                
    elif entrada[0] == "C":
        cont = 0
        for i in range(len(d.items)):
            if d.items[i] == entrada[1]:
                cont+=1
        print(cont)
        
    elif entrada[0] == "X":
        print()
        for i in range(len(d.items)):
            print(d.removeFront())
        

        
