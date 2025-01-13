#             1
#            /  \
#          2     3
#         /  \  /  \
#        4    5 6   7
class Node():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class tree():
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<root.data:
                root.left=self.rinsert(root.left,data)
            else:
                root.right=self.rinsert(root.right,data)
            return root
    def inorder(self):#left-->root-->right
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
            if root:
                self.rinorder(root.left,result)
                result.append(root.data)
                self.rinorder(root.right,result)

    def prorder(self):#root-->left-->right
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result=result.append(root.data)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):#left-->right-->root
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result=result.append(root.data)
cg=tree()
cg.insert(5)
cg.insert(4)
cg.insert(89)
cg.insert(3)
cg.insert(9)
cg.insert(5)
print(cg.inorder())


                

            