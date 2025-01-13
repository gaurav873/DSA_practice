# implementation of deque by using list
class Deque:
    def __init__(self):
        self.mylist=[]
    def is_empty(self):
        return len(self.mylist)==0
    def insert_front(self,data):  # front means oldest element
        self.mylist.insert(-1,data) #self.mylist=self.mylist+[data]
    def insert_rear(self,data):
        self.mylist.append(data)
    def delete_front(self):
        if not self.is_empty():
            return self.mylist.pop()
        else:
            raise IndexError('Deque is empty')
    def delete_rear(self):
        if not self.is_empty():
            return self.mylist.pop(0)
        else:
            raise IndexError('Deque is empty')
    def get_front(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError('Deque is empty')
    def get_rear(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError('Deque is empty')
    def size(self):
        return len(self.mylist)


# drivwer code
fg=Deque()
fg.insert_front(76)
fg.insert_front(98)
fg.insert_rear(34)
fg.insert_rear(56)
print(fg.size())
print(fg.get_front())
print(fg.get_rear())
fg.delete_front()
fg.delete_rear()
print(fg.size())

      

