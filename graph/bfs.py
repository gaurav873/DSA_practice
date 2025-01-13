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

# graph will return a dictionary---->{1:[(2,1),(3,1)],2:[(1,1),(3,1)]}
    def bfs(self,source_node):
        visited=[0*x for x in range(self.vno)]#[0,0,0]
        queue=[]
        queue.append(source_node)
        while queue:
            popped_node=queue.pop(0)
            if visited[popped_node-1]==0:
                print(popped_node,end='')
                visited[popped_node]=1
            for next_node,_ in self.dic[popped_node]:
                if visited[next_node-1]==0:
                    queue.append(next_node)
# depth first search--->major difference between dfs and bfs is dfs use-->stack and bfs use-->queue
    def bfs(self,source_node):
        visited=[0*x for x in range(self.vno)]#[0,0,0]
        stack=[]
        stack.append(source_node)
        while stack:
            popped_node=stack.pop()
            if visited[popped_node-1]==0:
                print(popped_node,end='')
                visited[popped_node]=1
            for next_node,_ in self.dic[popped_node]:
                if visited[next_node-1]==0:
                    stack.append(next_node)

# driver code