n = 4 #no.of nodes
graph = [[] for _ in range(n)] #graph with n nodes
visited = [False]*n # visited list with boolean

def addEdge(v,w):
    graph[v].append(w) # add directions to the graph

def DFS(node):
    visited[node] = True 
    print(node,end="  ")

    for adjcent in graph[node]:
        if not visited[adjcent]:
            DFS(adjcent) #recursive call for deapth

addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 2)
addEdge(2, 0)
addEdge(2, 3)
addEdge(3, 3)
DFS(2)
