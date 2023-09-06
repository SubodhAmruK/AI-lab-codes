import copy

graph = [[8, 3, 4], [1, 7, 2], [5, 6, 0]]  # initial state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # final state
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
    hs = 0
    for i in range(3):
        for j in range(3):
            if graph[i][j] != goal_state[i][j]:
                hs += 1
    return hs

def create():
    row_index = find_row_index(graph)
    col_index = find_col_index(graph)
    queue.append(copy.deepcopy(graph))
    print_graph(queue[0])
    while True:
        current_state = queue.pop(0)
        row_index = find_row_index(current_state)
        col_index = find_col_index(current_state)
        if current_state == goal_state:
            print("Goal state reached!")
            break
        if up(current_state, row_index, col_index):
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index - 1][col_index]
            current_state[row_index - 1][col_index] = temp
            print(find_heu(current_state))
            print_graph(current_state)
            queue.append(copy.deepcopy(current_state))
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index - 1][col_index]
            current_state[row_index - 1][col_index] = temp
        if left(current_state, row_index, col_index):
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index][col_index - 1]
            current_state[row_index][col_index - 1] = temp
            print(find_heu(current_state))
            print_graph(current_state)
            queue.append(copy.deepcopy(current_state))
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index][col_index - 1]
            current_state[row_index][col_index - 1] = temp
        if down(current_state, row_index, col_index):
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index + 1][col_index]
            current_state[row_index + 1][col_index] = temp
            print(find_heu(current_state))
            print_graph(current_state)
            queue.append(copy.deepcopy(current_state))
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index + 1][col_index]
            current_state[row_index + 1][col_index] = temp
        if right(current_state, row_index, col_index):
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index][col_index + 1]
            current_state[row_index][col_index + 1] = temp
            print(find_heu(current_state))
            print_graph(current_state)
            queue.append(copy.deepcopy(current_state))
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index][col_index + 1]
            current_state[row_index][col_index + 1] = temp

create()
