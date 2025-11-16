class Stack():

    def __init__(self, maxSize):

        self.items = []
        self.top_pointer = -1
        self.maxSize = maxSize
        

    def push(self, value):
        if self.IsFull():
            raise Exception("Stack is full")
        self.items.append(value)
        self.top_pointer += 1
        
    def pop(self):
        if self.IsEmpty():
            raise Exception("Stack is empty")
        self.top_pointer -= 1
        return self.items.pop()

    def peek(self):
        if self.IsEmpty():
            raise Exception("Stack is empty")
        return self.items[self.top_pointer]
        
    
    def IsFull(self):
        if len(self.items) >= self.maxSize:
            return True
        else:
            return False

    def IsEmpty(self):
        if self.top_pointer == -1:
            return True
        else:
            return False
        
    def showStack(self):
        return self.items
        

stack = Stack(3)
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.showStack())  # [10, 20, 30]
print(stack.peek())       # 30
print(stack.pop())        # 30
print(stack.showStack())  # [10, 20]
