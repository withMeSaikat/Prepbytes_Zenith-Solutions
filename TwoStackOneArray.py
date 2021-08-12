class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.front = -1
        self.back = self.size
        self.maxLenOfData = -1
        
    def enqueueFront(self, data):
        if self.back <= self.front + 1:
            print("Stack Full")
            return False
        
        self.front += 1
        self.stack[self.front] = data
        
        if len(str(data)) > self.maxLenOfData:
            self.maxLenOfData = len(str(data))
            
        return True
    
    def enqueueBack(self, data):
        if self.back <= self.front + 1:
            print("Stack Full")
            return False
        
        self.back -= 1
        self.stack[self.back] = data
        
        if len(str(data)) > self.maxLenOfData:
            self.maxLenOfData = len(str(data))
        
        return True
    
    def printStack(self):
        isEmpty = True
        
        if self.front >= 0:
            print("*" * (self.maxLenOfData + 4))
            for i in range(0, self.front + 1):
                print("* " + str(self.stack[i]) + " " * (self.maxLenOfData + 1 - len(str(self.stack[i]))) + "*")
            
            isEmpty = False
        
        if self.back < self.size:
            print("*" * (self.maxLenOfData + 4))
            for i in range(self.back, self.size):
                print("* " + str(self.stack[i]) + " " * (self.maxLenOfData + 1 - len(str(self.stack[i]))) + "*")
            
            isEmpty = False
        
        if not isEmpty:
            print("*" * (self.maxLenOfData + 4))
        else:
            print("Stack is Empty.")

def main():
    stack = Stack(10)
    stack.enqueueBack(5)
    stack.enqueueBack(7)
    #stack.printStack()
    stack.enqueueFront(2)
    stack.enqueueFront(3)
    stack.enqueueFront(111)
    stack.printStack()
    stack.enqueueBack(1234)
    stack.enqueueBack(00)
    stack.enqueueBack(128)
    stack.enqueueBack(11)
    stack.enqueueBack(14)
    stack.enqueueBack(98)
    stack.printStack()
if __name__ == "__main__":
    main()
                