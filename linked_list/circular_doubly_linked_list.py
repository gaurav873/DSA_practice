# circular doubly linked list
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class CDLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        new_node=Node(data)
        if not self.is_empty:
            new_node.prev=self.start.prev
            new_node.next=self.start
            if self.start.next==self.start:
                self.start.next=new_node
            else:
                self.start.prev.next=new_node
            self.start.prev=new_node
            self.start=new_node
        else:
            new_node.prev=new_node
            new_node.next=new_node
            self.start=new_node      
    def insert_at_last(self,data):
        new_node=Node(data)
        if not self.is_empty():
            new_node.prev=self.start.prev
            new_node.next=self.start
            self.start.prev.next=new_node
            self.start.prev=new_node
        else:
            new_node.prev=new_node
            new_node.next=new_node
            self.start=new_node
    def search(self,data):
        if not self.is_empty():
            temp=self.start
            while True:
                if temp.item==data:
                    return temp
                temp=temp.next
                if temp==self.start:
                    break
        else:
            return None
    def insert_after(self,data,search_data):
        if not self.is_empty():
            searched_node=self.search(search_data)
            if searched_node is not None:
                new_node=Node(None,data,None)
                new_node.prev=searched_node
                new_node.next=searched_node.next
                searched_node.next=new_node
                searched_node.next.prev=new_node
    def print_element(self):
        if not self.is_empty():
            temp=self.start
            print(temp,end=' ')
            temp=temp.next
            while not temp==self.start:
                print(temp,end=" ")
                temp=temp.next
        else:
             return None
    def delete_at_start(self):
        if not self.is_empty():
            if self.start.prev==self.start:
                self.start=None
            else:
                self.start.next.prev=self.start.prev
                self.start.prev.next=self.start.next
                self.start=self.start.next
    def delete_at_last(self):
        if not self.is_empty():
            if self.start.prev==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
    def delete_item(self,search_data):
        search_Node=self.search(search_data)
        if search_Node is not None:
            if self.start.prev==self.start and self.start==search_Node:# when list have only one node
                self.start=None
            else:
                search_Node.prev.next=search_Node.next  # this part is for middle part 
                search_Node.next.prev=search_Node.prev
                if search_Node==self.start: # this part for the first node will be searched node  
                    self.start=self.start.next
        else:
            return None
    def __iter__(self):
        return CDLLITERATOR(self.start)


class CDLLITERATOR():
    def __init__(self,start):
        self.current=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data=self.current.item
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
            data=self.current.item
            self.current=self.current.next
            return data 

        

        


    
            




            





            







            






        
           