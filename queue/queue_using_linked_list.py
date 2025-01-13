# queue using linked list
class Node():
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None # front means oldest element
        self.rear=None  # rear means newest element
        self.count=0 
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n 
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1
    def dequeue(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
            self.count-=1
        else:
            raise IndentationError('Queue is empty')
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndentationError('Queue is empty')
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndentationError('Queue is empty')
    def size(self):
        return self.count
    
#driver code
fg=Queue()
fg.enqueue(45)
fg.enqueue(34)
fg.enqueue(78)
print(fg.size())
fg.dequeue()
print(fg.get_front())
print(fg.get_rear())
print(fg.size())
    




            
        

            
            

