import copy
graph = [[8, 3, 4], [1, 7, 2], [5, 6, 0]] #intial state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #final state
level = 3 # no of levels
queue = []
n = 2
def print_graph(graph):
    for row in graph:
        for col in row:
            print(col, end=" ")
        print()
    print()

def up(graph, row_index, col_index):
    if row_index - 1 >= 0:
        return True
    return False

def down(graph, row_index, col_index):
    if row_index + 1 <= n:
        return True
    return False

def left(graph, row_index, col_index):
    if col_index - 1 >= 0:
        return True
    return False

def right(graph, row_index, col_index):
    if col_index + 1 <= n:
        return True
    return False

def find_row_index(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return i
    return -1

def find_col_index(matrix):
    for row in matrix:
        for j in range(len(row)):
            if row[j] == 0:
                return j
    return -1

def find_heu(graph):
    i=0
    hs = 0
    for i in range(3):
        for j in range(3):
            if graph[i][j] != goal_state[i][j]:
                hs+=1
    return hs

def create():
    row_index = find_row_index(graph)
    col_index = find_col_index(graph)
    #print(find_heu(m))
    queue.append(copy.deepcopy(graph))
    print_graph(queue[0])
    b=1
    for i in range(4):
        k=0
        print("Level : ",(i+1))
        while b>0:
            a = queue[0]
            if up(a, row_index, col_index):
                k+=1
            if down(a, row_index, col_index):
                k+=1
            if right(a, row_index, col_index):
                k+=1
            if left(a, row_index, col_index):
                k+=1
            b-=1
        print(k)
        while k>0:
            m = queue.pop(0)
            
            row_index = find_row_index(m)
            col_index = find_col_index(m)
            if m == 0:
                break
            if up(m, row_index, col_index):
                temp = m[row_index][col_index]
                m[row_index][col_index] = m[row_index - 1][col_index]
                m[row_index - 1][col_index] = temp
                print(find_heu(m))
                print_graph(m)
                queue.append(copy.deepcopy(m))
                temp = m[row_index][col_index]
                m[row_index][col_index] = m[row_index - 1][col_index]
                m[row_index - 1][col_index] = temp
                b+=1
            k-=1
            if left(m, row_index, col_index):
                temp = m[row_index][col_index]
                m[row_index][col_index] = m[row_index][col_index - 1]
                m[row_index][col_index - 1] = temp
                print(find_heu(m))
                print_graph(m)
                queue.append(copy.deepcopy(m))
                temp = m[row_index][col_index]
                m[row_index][col_index] = m[row_index][col_index - 1]
                m[row_index][col_index - 1] = temp
                b+=1
            k-=1
            if down(m, row_index, col_index):
                temp = m[row_index][col_index]
                m[row_index][col_index] = m[row_index + 1][col_index]
                m[row_index + 1][col_index] = temp
                print(find_heu(m))
                print_graph(m)
                queue.append(copy.deepcopy(m))
                temp = m[row_index][col_index]
                m[row_index][col_index] = m[row_index + 1][col_index]
                m[row_index + 1][col_index] = temp
                b+=1
            k-=1
            if right(m, row_index, col_index):
                temp = m[row_index][col_index]
                m[row_index][col_index] = m[row_index][col_index + 1]
                m[row_index][col_index + 1] = temp
                print(find_heu(m))
                print_graph(m)
                queue.append(copy.deepcopy(m))
                temp = m[row_index][col_index]
                m[row_index][col_index] = m[row_index][col_index + 1]
                m[row_index][col_index + 1] = temp
                b+=1
            k-=1
            
            

create()