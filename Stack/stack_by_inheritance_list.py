#Implmentation of stack by inheirting list
class Stack(list):# stack is the child class of list(parentclass)
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if  not self.is_empty():
          return super().pop()
        else:
            raise IndexError('stack is empty')
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('stack is empty')
    def size(self):
        return len(self)
    def insert(self,data,index):
        raise AttributeError('NO attribute insert in stack')
#driver Code
sl=Stack()
sl.push(44)
sl.push(55)
sl.push(35)
sl.push(89)
print(sl.peek())
#sl.insert(445,2)
sl.pop()

    