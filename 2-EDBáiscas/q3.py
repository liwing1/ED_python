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

n = input()

for i in n:
    if i != "*":
        s.push(i)
    else:
        print(s.pop(), end="")