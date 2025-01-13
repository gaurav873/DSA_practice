# Stack implementation by inheirtance singly linked list
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from linked_list.Singly_linked_list import *
class Stack(SLL):
    #count=0 -->class variable when i make multiple stack instance, the count variable will be incrementd and decremented for all instances 
    def __init__(self,):
        super().__init__()
        self.count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.count +=1
        return self.append(data)    
    def pop(self):
        if not self.is_empty():
            self.count -=1
            return self.delete_first()
    def peek(self):
        if not self.is_empty():
            temp=self.start.item
            return temp
        else:
            raise AttributeError('Stack is empty')
    def size(self):
        return self.count

# driver code
sl=Stack()
sl.push(34)
sl.push(55)
sl.push(78)
print(sl.size())
sl.pop()
print(sl.peek())
print(sl.size())







