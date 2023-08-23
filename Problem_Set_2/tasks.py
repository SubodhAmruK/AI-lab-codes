def canFinish(tasks, prerequisites):
    graph = [[] for _ in range(tasks)]
    visited = [False]*tasks
    degree = [0]*tasks
    node = -1
    for i in prerequisites:
        u,v = i
        graph[v].append(u)
        degree[u]+=1

    for i in range(tasks): #Finds the first node with degree 0
        if degree[i] == 0:
            node = i
            
    if node == -1:
        return False
    else:
        def DFS(node):
            visited[node] = True
            for i in graph[node]:
                if not visited[i]:
                    DFS(i)
                else:
                    return False
    return True

print(canFinish(2, [[0, 1], [1, 0]]))  # Output: False
print(canFinish(3, [[1, 0], [0, 2]]))  # Output: True
print(canFinish(4,[[0, 1], [1, 2], [2, 3]]))
print(canFinish(3,[[0, 1], [1, 2], [2, 0]]))
print(canFinish(3,[]))
print(canFinish(5,[[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]]))
print(canFinish(6,[[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 5]]))
print(canFinish(5,[[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]]))

