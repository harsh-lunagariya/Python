class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue)==0
    
    def print(self):
        print(self.queue)

if __name__=="__main__":
    q = Queue()
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q.dequeue())
    print(q.is_empty())
    print(q.size())
    q.print()