class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        newstack = []
        while self.queue:
            newstack.append(self.queue.pop())
        newstack.pop()
        while newstack:
            self.queue.append(newstack.pop())
        # self.queue.pop(0)

    # @return an integer
    def peek(self):
        newstack = []
        while self.queue:
            newstack.append(self.queue.pop())
        # newstack.pop()
        value = newstack[-1]
        while newstack:
            self.queue.append(newstack.pop())
        
        return value
        

    # @return an boolean
    def empty(self):
        if not self.queue:
            return True
        else:
            return False
        
