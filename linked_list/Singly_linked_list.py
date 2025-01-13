# singly linked list 
class Node:
    def __init__(self,item=None,next=None):
        self.item=item # instance object variable
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start= start 
    def is_empty(self):
        return self.start is None
    def append(self,data):
        n=Node(data,self.start) 
        self.start=n
        # first we call node class then we item will be data and in next  variable there is the reference of self.start
    def at_last(self,data):
        n=Node(data) # by default next value will be none
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
                
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp.next is not None:
            if temp.item==data:
                 return temp
            temp=temp.next
        return None

    def insert_after(self,data,data_after):
        n=Node(data)
        a=self.search(data_after)
        if a is not None:
            n.next=a.next
            a.next=n
            return 
        else:
             return (f"Error: {data_after} not found in the list")
    def print_element(self):
        if self.start is not None:
            temp=self.start
            while temp.next is not None:
                print(temp.item,end=' ')
                temp=temp.next
        else:
             pass
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is not None:
            pass
        elif self.start.next is None:
            pass
        else:
             temp=self.start
             while temp.next.next  is not None:
                temp=temp.next
             temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
            else:
                pass
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next


            


            

        
             


            
            
    

        
    

                    
            


#if __name__=='main':
# driver code
sll=SLL()
sll.append(4)
sll.append(85)
sll.at_last(56)
sll.search(56)
sll.insert_after(78,85)
print(sll)
sll.delete_last()
print(sll)






        

    