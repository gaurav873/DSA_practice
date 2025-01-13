#Doubly_linked_list
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
           self.start.prev=n  
           #self.start=n
           # #else:
           # #self.start=n  that menas same 
        self.start=n        
    def insert_at_last(self,data):
        n=Node(None,data,None)                  
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.prev=temp
        else:
            self.start=n 
   #temp=self.start
    #    if self.start is not None:
     #       while temp.next is not None:
      #          temp=temp.next
       # n=Node(temp,data,None)
        #if temp==None:
         #   self.start=n
        #else:
         # temp.next=n 
    def search(self,data):
        temp=self.start   
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,data,data_after):
        n=Node(None,data,None)
        temp=self.search(data_after)
        if temp is not None:
            n.prev=temp.next
            temp.next=n
            if temp.next is not None:
                temp.next.prev=n
            else:
                n.next=None
        else:
            return (f"Error: {data_after} not found in the list")
    def print_element(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            temp=self.start
            if temp.next is not None:
                self.start=temp.next # there is something to change
                temp.next.prev=None
            else:
                self.start=None
        else:
            pass
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def delete_item(self,data):
        n=self.search(data)
        if n != None:
            if n.prev==None:
                self.start=n.next
                if n.prev==None and n.next != None:
                    self.start.next.prev=None
            elif n.next==None:
                n.prev.next=None
            else:
                n.prev.next=n.next
                n.next.prev=n.prev
        else:
            pass
# driver code
f=DLL()
f.insert_after(345,44)
f.print_element()
f.insert_at_start(78)
f.insert_at_last(44)
f.print_element()
