# implemnetation of priority queue using list
class Priority_queue():
    def __init__(self):
        self.mylist=[]
    def is_empty(self):
        return len(self.mylist)==0
    def push(self,data,priority_number):
        index=0        
        while index<len(self.mylist) and self.mylist[index][1]<=priority_number:#it basically a nested tuple in a list, this line compare therir priority number
                index+=1
        self.mylist.insert(index,(data,priority_number))
    def pop(self):
        if self.is_empty():
             raise IndexError('priority_Queue is empty')
        else:
             return self.mylist.pop(0)[0]# self.mylist.pop(0) it pop the element and [0] it show the value on that index. 
    def size(self):
         return len(self.mylist)
    
# driver code
fg=Priority_queue()
fg.push('gaurav',2)         
fg.push('masnhi',5)         
fg.push('shivam',3)         
fg.push('jai',4)  
while not fg.is_empty():
    print(fg.pop())       
            
            
                
        
        



        