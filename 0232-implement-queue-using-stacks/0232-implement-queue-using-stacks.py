class MyQueue:

    def __init__(self):
        self.arr=[0]*1000
        self.rear=0
        self.front=0
        
    # push element at back of the queue
    def push(self, x: int) -> None:
        if (self.isFull()):
            return
        self.arr[self.rear]=x
        self.rear+=1
    def isFull(self) ->bool:
        if self.rear==1000:
            return True
        return False

# removes element from front of the queue and returns it
    def pop(self) -> int:
        if(self.empty()):
            return 
        temp=self.arr[self.front]
        self.front+=1
        return temp
    def empty(self) -> bool:
        if self.rear==self.front:
            return True
        else:
            return False
    # returns the element at the front of the queue
    def peek(self) -> int:
        if self.empty():
            return 
        return self.arr[self.front]


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()