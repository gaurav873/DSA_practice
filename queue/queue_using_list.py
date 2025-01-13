# queue using list
class Queue():
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Queue is empty')
    def get_front(self):  # front means oldest element
        if not self.is_empty():
            return self.items[-1]
            
        else:
            raise IndexError('Queue is empty')
    def get_rear(self):# rear means newest element
        if not self.is_empty():
            temp=self.items
            return temp[0]
        else:
            raise IndexError('Queue is empty')
    def size(self):
        return len(self.items)
fg=Queue()
try:
    fg.enqueue(56)
    fg.enqueue(67)
    fg.enqueue(87)
    print(fg.size())
    print(fg.is_empty())
    fg.dequeue()
    print(fg.size())
    print(fg.get_front())
    print(fg.get_rear())
except IndexError as e:
    print(e.args[0])



    
        








