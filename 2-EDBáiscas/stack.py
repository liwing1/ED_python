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
    
    def get_stack(self):
        return self.items    


s = Stack() 
s.push(0)
s.push(2)
s.pop()
s.pop()
for i in s.items:
    print(i)
    
