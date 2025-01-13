# implementation of deque with the help of doubly linked list
class Node():
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=item
class Deque():
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    def is_empty(self):
        return self.front==None
    def insert_rear(self,data):
        new_node=Node(self.rear,data,None)
        self.count+=1
        if self.is_empty():
            self.front=new_node
        else:
            self.rear.next=new_node
        self.rear=new_node
    def insert_front(self,data):
        new_node=Node(None,data,None)
        new_node.next=self.front
        self.count+=1
        if self.is_empty():  
            self.rear=new_node
        else:
            self.front.prev=new_node
        self.front=new_node
        new_node.prev=None
    def delete_front(self):
        if not self.is_empty():
            self.count-=1
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                temp=self.front
                self.front=self.front.next
                self.front.prev=None
                temp.next=None
        else:
            raise IndexError('Queue is empty')
    def delete_rear(self):
        if not self.is_empty():
            self.count-=1
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.rear=self.rear.prev
                if self.rear:
                    self.rear.next=None
        else:
            raise IndexError('Queue is empty')
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError('Queue is empty')
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError('Queue is empty')
    def size(self):
        return self.count
# driver code
fg=Deque()
fg.insert_rear(45)
fg.insert_front(56)
fg.insert_rear(78)
fg.insert_rear(23)
print(fg.size())
fg.delete_front()
fg.delete_rear()
print(fg.get_front())
print(fg.get_rear())
print(fg.size())
        






    


