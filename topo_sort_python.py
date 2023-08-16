n = 6
graph = [[] for i in range(6)]
visited = [False]*n
stack = []

def addEdge(v,w):
    graph[v].append(w)

def DFS(n):
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            DFS(i)
    
    stack.append(n)

def topoSearch():
    for i in range(n):
        if not visited[i]:
            DFS(i) 
    print(stack[::-1])

addEdge(5, 2)
addEdge(5, 0)
addEdge(4, 0)
addEdge(4, 1)
addEdge(2, 3)
addEdge(3, 1)

topoSearch()