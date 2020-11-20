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

def isPalindrome(entrada):
    return entrada == entrada[::-1]


for entrada in input().split():
    palindromes = set()
    for cont in range(len(entrada), 2, -1):
        for i in range(len(entrada) - cont + 1):
            slice = entrada[i:cont + i]
            if isPalindrome(slice) and not any(slice in k for k in palindromes):
                palindromes.add(slice)
    if len(palindromes) > 1:
        print(entrada)