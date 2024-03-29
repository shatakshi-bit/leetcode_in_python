class MyCircularQueue:

    def __init__(self, p: int):
        self.array = [0] * p
        self.rear = -1
        self.size = 0
        self.c = p

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.rear = (self.rear + 1) % self.c
        self.array[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.array[(self.rear-self.size+1) % self.c]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.array[self.rear]

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size == self.c