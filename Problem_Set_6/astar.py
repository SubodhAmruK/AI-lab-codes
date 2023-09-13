import copy

graph = [[8, 3, 4], [1, 7, 2], [5, 6, 0]]  # initial state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # final state
level = 4  # no of levels
queue = [] # queue
n = 2 # size of matrix
g=0 # calculates g(n)

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
    i = 0
    hs = 0
    for i in range(3):
        for j in range(3):
            if graph[i][j] != goal_state[i][j]:
                hs += 1
    return hs
def next_state(graph,next_hs):
    hs = find_heu(graph)
    fs = hs+g
    if next_hs==-1:
        next_hs = fs
    elif fs<=next_hs:
        next_hs = fs
        next_trav = copy.deepcopy(graph)

def create(g):
    row_index = find_row_index(graph)
    col_index = find_col_index(graph)
    queue.append(copy.deepcopy(graph))
    print_graph(queue[0])
    for i in range(level):
        next_hs = -1
        next_trav = 0
        print("Level : ", (i + 1))
        g+=1
        num_nodes_at_level = len(queue)
        for j in range(num_nodes_at_level):
            current_state = queue.pop(0)
            row_index = find_row_index(current_state)
            col_index = find_col_index(current_state)
            if up(current_state, row_index, col_index):
                temp = current_state[row_index][col_index]
                current_state[row_index][col_index] = current_state[row_index - 1][col_index]
                current_state[row_index - 1][col_index] = temp
                hs = find_heu(current_state)
                fs = hs+g
                next_state(current_state,next_hs)
                #print("H(s) : ",hs)
                #print("G(s) : ",g)
                #print("F(s) : ",hs+g)
                #print()
                #print_graph(current_state)
                #queue.append(copy.deepcopy(current_state))
                temp = current_state[row_index][col_index]
                current_state[row_index][col_index] = current_state[row_index - 1][col_index]
                current_state[row_index - 1][col_index] = temp
            
            if left(current_state, row_index, col_index):
                temp = current_state[row_index][col_index]
                current_state[row_index][col_index] = current_state[row_index][col_index - 1]
                current_state[row_index][col_index - 1] = temp
                hs = find_heu(current_state)
                fs = hs+g
                next_state(current_state,next_hs)
                #print("H(s) : ",hs)
                #print("G(s) : ",g)
                #print("F(s) : ",fs)
                #print()
                #print_graph(current_state)
                #queue.append(copy.deepcopy(current_state))
                temp = current_state[row_index][col_index]
                current_state[row_index][col_index] = current_state[row_index][col_index - 1]
                current_state[row_index][col_index - 1] = temp
            if down(current_state, row_index, col_index):
                temp = current_state[row_index][col_index]
                current_state[row_index][col_index] = current_state[row_index + 1][col_index]
                current_state[row_index + 1][col_index] = temp
                hs = find_heu(current_state)
                fs=hs+g
                next_state(current_state,next_hs)
                #print("H(s) : ",hs)
                #print("G(s) : ",g)
                #print("F(s) : ",fs)
                #print()
                #print_graph(current_state)
                #queue.append(copy.deepcopy(current_state))
                temp = current_state[row_index][col_index]
                current_state[row_index][col_index] = current_state[row_index + 1][col_index]
                current_state[row_index + 1][col_index] = temp
            if right(current_state, row_index, col_index):
                temp = current_state[row_index][col_index]
                current_state[row_index][col_index] = current_state[row_index][col_index + 1]
                current_state[row_index][col_index + 1] = temp
                hs = find_heu(current_state)
                fs = hs+g
                next_state(current_state,next_hs)
                #print("H(s) : ",hs)
                #print("G(s) : ",g)
                #print("F(s) : ",hs+g)
                #print()
                #print_graph(current_state)
                #queue.append(copy.deepcopy(current_state))
                temp = current_state[row_index][col_index]
                current_state[row_index][col_index] = current_state[row_index][col_index + 1]
                current_state[row_index][col_index + 1] = temp
        hs = find_heu(next_trav)
        fs = hs+g
        print("H(s) : ",hs)
        print("G(s) : ",g)
        print("F(s) : ",fs)
        print()
        queue.append(copy.deepcopy(next_trav))
        print(next_trav)

create(g)
