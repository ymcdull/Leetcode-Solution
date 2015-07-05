class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        for i in xrange(len(self.stack)-1):
            self.stack.append(self.stack.pop(0))
        self.stack.pop(0)
        

    # @return an integer
    def top(self):
        return self.stack[-1]
        

    # @return an boolean
    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
