class Queue():

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.top_pointer = -1
        self.rear_pointer = -1
        self.items = []

    def enqueue(self, item):
        if self.isFull():
            raise Exception("Queue is full")

        self.items.append(item)
        self.rear_pointer += 1
        
        if self.top_pointer == -1:
            self.top_pointer = 0

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        
        remove = self.items[self.top_pointer]
        self.top_pointer += 1
        
        if self.top_pointer > self.rear_pointer:
            self.top_pointer = -1
            self.rear_pointer = -1

        return remove

    def isEmpty(self):
        return self.top_pointer == -1  

    def isFull(self):

        if self.top_pointer == -1:
            return False
        return (self.rear_pointer - self.top_pointer + 1) >= self.maxSize

    def showQueue(self):

        if self.isEmpty():
            return []
        return self.items[self.top_pointer:self.rear_pointer + 1]