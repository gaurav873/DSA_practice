#binary searach tree using doubly linked list
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.item:
            root.left=self.rinsert(root.left,data)
        else:
            root.right=self.rinsert(root.right,data)
        return root
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        #base case
        if root==None or root.item==data:
            return root
        if data<root.item:
            return self.rsearch(root.left,data)
        else :
            return self.rsearch(root.right,data)
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):#left-->root-->right
        # base case
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def postorder(self):#left-->right-->root
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):#
        #base case
        self.rpostorder(root.left,result)
        self.rpostorder(root.right,result)
        result.append(root.item)
    def preorder(self):#root-->left-->right
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root is not None:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    # find minimum value item node
    # recurssive approach
    def minimum_node(self):
        return self.rmini_node(self.root)
        # humme root.left find krni ha jb tk vo none na ho je 
        # base case jb loop close hoga
    def rmini_node(self,root):
        if root.item==None:
            return 'Tree is empty'
        if root.left==None:
            return root.item
        else:
            self.rmini_node(root.left)
    # iteration approach
    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.left

    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.right

    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        if data<root.item:
            root.left=self.rdelete(root.left,data)
        elif data>root.item:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.min_value(root.right)
            self.rdelete(root.right,root.item)
        return root
    def size(self):
        return len(self.preorder())
cg=BST()
cg.insert(4)
cg.insert(5)
cg.insert(3)
cg.insert(6)
cg.insert(2)
print(cg.inorder())
print(cg.size())
print(cg.delete(3))
print(cg.size())
    



 

    

        

            





        
        
         
