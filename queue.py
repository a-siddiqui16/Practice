class Queue():

    def __init__(self, maxSize):

        self.maxSize = maxSize
        self.top_ponter = -1
        self.rear_pointer = -1
        self.items = []

    def enqueue(self, item):

        if self.isFull():
            raise Exception("Queue is full")

        self.items.append(item)
        self.top_ponter = 0

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        
        self.items.remove(self.items[self.top_ponter])
        self.top_ponter += 1

    def isEmpty(self):
        if self.rear_pointer == -1:
            return True
        else:
            return False

    def isFull(self):
        if len(self.items) >= self.maxSize:
            return True
        else:
            return False

    def showQueue(self):
        return self.items
    

queue = Queue(6)

queue.enqueue(5)
queue.enqueue(6)
queue.dequeue()
queue.showQueue()