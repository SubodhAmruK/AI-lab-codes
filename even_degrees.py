n,m = map(int,input("Enter the values of N and M : ").split())
u,v=0,0
degree = [0]*(n)
graph = [-1]*m
print(degree)
print(graph)

if(m%2!=0 and n%2!=0):
    print(-1)
else:
    for i in range(m):
        u,v = map(int,input("Enter the values of vertices to connect : ").split())
        if degree[u-1] %2 == 0 and degree[v-1] %2 == 0:
            graph[i] = 0;
            degree[v-1]+=1
        elif degree[u-1] %2 != 0 and degree[v-1] %2 == 0:
            graph[i] = 1;
            degree[u-1]+=1
        elif degree[u-1] %2 == 0 and degree[v-1] %2 != 0:
            degree[v-1]+=1    
            graph[i] = 1;
        elif degree[u-1] %2 != 0 and degree[v-1] %2 != 0:
            degree[v-1]+=1 
    for i in degree:
        if i%2 !=0:
            print(-1)
            exit(0);
    
    print(graph)
