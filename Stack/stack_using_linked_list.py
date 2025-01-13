#implemenatation of stack using linked list
class Node():
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack():
    def __init__(self):
        self.start=None
    def is_empty(self):
        return self.start==None
    def push(self,data):
        New_node=Node(data,self.start)
        self.start=New_node
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            return data
        else:
            raise IndexError('stack is empty')
    def peek(self):
        if not self.is_empty():
            data=self.start.item
            return data
        else:
            raise IndexError('stack is empty')
    def size(self):
        temp=self.start
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        return count
# driver code
sl=Stack()
sl.push(45)
sl.push(10)
sl.push(20)
print(sl.size())
print(sl.peek())
print(sl.pop())
        

