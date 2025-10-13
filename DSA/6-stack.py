from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,data):
        self.container.append(data)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def print(self):
        print(self.container)
    
if __name__=="__main__":
    s = Stack()
    s.push(4)
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(6)
    print(s.pop())
    print(s.peek())
    s.print()