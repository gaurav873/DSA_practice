# circular linked list
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,tail=None):
        self.tail=tail
    def is_empty(self):
        return self.tail==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.tail is not None:
            n.next=self.tail.next
            self.tail.next=n
        else:
            self.tail=n
            n.next=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.tail is not None:
            n.next=self.tail.next
            self.tail.next=n
            self.tail=n
        else:
            self.tail=n
            n.next=n
    def search(self,data):
        if self.is_empty():
            return None 
        else:
            temp=self.tail.next
            while temp!=self.tail:
                if temp.item==data:
                    return temp
                temp=temp.next
            if temp==data:
                return temp
            else:
                pass    

    def insert_item(self,data,search_data):
        temp=self.seach(search_data)
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.tail:
                self.tail=n
        else:
            pass
 #       new_node=Node(data)
  #      temp=self.search(search_data)
   #     if temp==None:
    #        return None
     #   elif temp==self.tail:
      #      new_node=temp.next
       #     temp.next=new_node
        #    self.tail=new_node
        #else:
         #   new_node=temp.next
          #  temp.next=new_node
    def print_list(self):
        if not self.is_empty():
            temp=self.tail.next
            while temp !=self.tail:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item)
        else:
            pass
    def delete_start(self):
        if not self.is_empty():
            if self.tail.next==self.tail:
                self.tail=None
            else:
                self.tail.next=self.tail.next.next
        else:
            pass
    def delete_last(self):
        if not self.is_empty():
            if self.tail.next==self.tail:
                self.tail=None
            else:
                temp=self.tail.next
                while temp.next!=self.tail:
                    temp=temp.next
                temp.next=self.tail.next
                self.tail=temp
        else:
            pass
    def delete_item(self,data):
        if not  self.is_empty():
            deleted_node=self.search(data)
            if deleted_node is not None:
                if deleted_node==self.tail:
                    return self.delete_last()
                else:
                    temp=self.tail.next
                    while temp.next !=deleted_node:
                        temp=temp.next
                    temp.next=deleted_node.next
        else:
            pass

 















        
        


        

        

    

