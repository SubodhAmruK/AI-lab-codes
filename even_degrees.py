n = int(input("Enter no.of vertices : "))
m = int(input("Enter no.of Edges : "))
degrees = [0]*n
graph = [[] for _ in range(n)]


if(m%2 != 0):
    print("-1")
else:
    for i in range(m):
        print("Enter connection between nodes. Edge {} : ".format(i+1))
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        if (u == v):
            print("No self loops allowed")
            break
        else:
            graph[u].append(v)
    
    for i in range(n):
        degrees[i] = len(graph[i])

print(degrees)
print(graph)