class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()

for i in input():
    if str.isdigit(i):
        d.addRear(i)
    elif i == "*":
        print(d.removeFront(), end = "")
    elif i == "+":
        print(d.removeRear(), end = "")
    else:
        d.addFront(i)
        
