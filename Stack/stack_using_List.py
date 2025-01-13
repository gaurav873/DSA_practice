#stack using list
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        return self.items.append(data )
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Stack is Empty')
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            raise IndexError('Stack is Empty')
    def Size(self):
        return len(self.items)
st=Stack()
st.push(40)
st.push(89)
st.push(45)
st.push(34)
print(st.peek())
print(st.pop())
print()
   
