# Linked List

# add - add value in the list
# insert_at - insert value at given index
# insert_values - insert multiple values in form of list or tuple
# insert_at_beginning 
# remove - remove given value
# remove_at - remove value at given index
# is_empty - list empty or not
# find - find index of given element
# print - print the Linked List
# len - give length of list
# clear - clear list


class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def add(self,data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    def print(self):
        if self.is_empty() == True:
            print("Linked List is empty")
            return
        itr = self.head
        LLstr = ''

        while itr:
            LLstr += str(itr.data) + '-->'
            itr = itr.next
        print(LLstr)

    def insert_values(self,data_set):
        if self.head != None :
            itr = self.head
            while itr.next:
                itr = itr.next
        for data in data_set:
            self.add(data)
    
    def is_empty(self):
        if self.head == None :
            return True
        else:
            return False
    
    def len(self):
        if self.is_empty():
            return 0
        else:
            count = 0
            itr = self.head
            while itr:
                count += 1
                itr = itr.next
            return count
    
    def remove_at(self,index):
        if index<0 or index>=self.len():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head = self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count+=1

    def find(self,data):
        index = -1
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                index=count
                break
            itr=itr.next
            count+=1
        return index
    
    def remove(self,data):
        index = self.find(data)
        if index == -1:
            print("Element not found")
            return
        self.remove_at(index)

    def insert_at(self,index,data):
        if index<0 or index>self.len():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_beginning(data)
        count=0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            count+=1
            itr = itr.next
    
    def clear(self):
        self.head = None

if __name__=="__main__":
    ll = LinkedList()
    ll.insert_values([10,20,30,40,50,60,70])
    ll.remove(0)
    ll.print()
    ll.clear()
    ll.print()

