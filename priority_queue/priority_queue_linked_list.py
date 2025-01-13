# implementation of priority queue using linked list
class Node():
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next 
class priority_queue():
    def __init__(self):
        self.start=None
        self.count=0
    def is_empty(self):
        return self.start==None
    def push(self,data,priority_number):
        new_node=Node(data,priority_number)
        self.count+=1
        if self.is_empty() or priority_number>self.start.priority:
            new_node.next=self.start
            self.start=new_node
        else:
            temp=self.start
            while temp.next is not None and new_node.priority>=temp.next.priority:
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def pop(self):
        if not self.is_empty():
            self.count-=1
            deleted_node=self.start.item
            self.start=self.start.next
            return deleted_node  
        else:
            raise IndexError("priority queue is empty")
    def size(self):
        return self.count
# driver code
fg=priority_queue()
fg.push("gaurav",4)
fg.push("hemant",3)
fg.push('shivam',1)
while not fg.is_empty():
    print(fg.pop())
    
    



