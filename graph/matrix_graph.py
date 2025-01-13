#adjacency matrix implementation
class Graph:
    def __init__(self,vno=None):
        self.vno=vno# hum yha bta denge kitne element honge hamare graph main.
        self.matrix=[[0]*vno for _ in range(vno)] # yeh utne element ki nested list bna denga.
    def insert_Node(self): # ismian yeh chate ha ek node bad zaye but uski but vo unconnected ho.
        self.vno+=1
        for nested_list in self.matrix:
            nested_list.append(0)
        new_nested_list=[0]*self.vno
        return self.matrix.append(new_nested_list)
    def add_edge(self,u,v,weight=1): # hume issmain connection create krna ha 
        if 0<=u<self.vno and 0<=v<self.vno:
            self.matrix[u][v]=weight
            self.matrix[v][u]=weight
        else:
            raise AttributeError
    def remove_edge(self,u,v):# isamin bss humme connection break krna ha 
        if 0<=u<self.vno and 0<=v<self.vno:
            if self.matrix[u][v] !=0 and self.matrix[v][u]!=0:
                self.matrix[u][v]=0
                self.matrix[v][u]=0
            else:
                print(f"No edge between vertex {u} and vertex {v}")
        else:
            raise IndexError("Vertex index out of range")
    def has_edge(self,u,v):
        if 0<=u<self.vno and 0<=v<self.vno:
            return self.matrix[u][v]<=1
        else:
            raise IndexError("Vertex index out of range")
    def print_adj_matrix(self):
        print('adjacency matrix')
        for nested_list in self.matrix:
            print(' '.join(str(element) for element in nested_list))
            #print(''.join(map(str,matrix)))
cg=Graph(4)
cg.print_adj_matrix()
cg.add_edge(0,3)
cg.add_edge(2,3)
cg.add_edge(3,1)
cg.print_adj_matrix()


            
        
    
        
        


        

             

        


    



        








             