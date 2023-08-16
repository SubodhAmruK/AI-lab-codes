n=4             # No.of nodes
graph = [[] for _ in range(n)]
visited = [False]*n   # List for visited nodes with the size n.
queue = []     #Initialize a queue


def addEdge(v,w):
  graph[v].append(w) # Adds edges to the list

def bfs(node): #function for BFS
  visited[node] = True;
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = "   ") 

    for adjcent in graph[m]:
      if not visited[adjcent]:
        visited[adjcent] = True
        queue.append(adjcent)

addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 2)
addEdge(2, 0)
addEdge(2, 3)
addEdge(3, 3)

bfs(2)