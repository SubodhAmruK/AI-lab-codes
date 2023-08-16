n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
graph = [0] * n

def addEdge():
    global graph
    for i in range(m):
        print("Enter the connecting nodes for Edge {}:".format(i + 1))
        print("Edge {}:".format(i + 1))
        u = int(input())
        v = int(input())
        if u == v:
            print("No self loops allowed")
            addEdge()
        graph[u] += 1
        graph[v] += 1

def verCheck():
    global graph
    for i in graph:
        if i % 2 != 0:
            print(-1)
            return

def dirEdges():
    for i in range(m):
        print(i % 2, end=" ")

# Adding edges to the graph
addEdge()

# Checking if even degrees are possible
verCheck()

# Printing directed edges
dirEdges()
