# graph using adjacent list
class Graph:
    def __init__(self,vno=1):# humne phele se hi ek elements dic main add kr diya
        self.vno=vno
        self.dic={elements:[] for elements in range(1,vno+1)}
    def add_nodes(self):
        self.vno+=1
        return self.dic.update({self.vno:[]})
    def has_edge(self,u,v):
         if u not in self.dic and v not in self.dic:
            # checking adjacnet nodes
            return False
         return u in [node for node,_ in self.dic[v]] and v in [node for node,_ in self.dic[u]]
    def add_edges(self,u,v,weight=1):
        if u in self.dic and v in self.dic:
            if not self.has_edge(u,v):
                self.dic[u].append((v,weight))
                self.dic[v].append((u,weight))
            else:
                print(f'edge{u} is already connected with{v}')
        else:
            raise AttributeError
    def remove_edges(self,u,v):
        if u in self.dic and v in self.dic:
            if self.has_edge(u,v):
                edge_u_v=[(node,weight)for node,weight in self.dic[u] if node==v]
                edge_v_u=[(node,weight)for node,weight in self.dic[v] if node==u]
                self.dic[u].remove(edge_u_v[0])
                self.dic[v].remove(edge_v_u[0])
            else:
                print(f'edge{u} is already connected with{v}')
        else:
            raise AttributeError
    def print_graph(self):
        print('Adjacent list')
        for vertex in self.dic.keys():
            if self.dic[vertex]:
                for x,_ in self.dic[vertex]:
                    print(f"{vertex}:{x}")
            else:
                print(f'{vertex}:no edges')
g=Graph(4)
print(g.print_graph())
g.add_nodes()
g.add_edges(2,3)
print(g.print_graph())
    