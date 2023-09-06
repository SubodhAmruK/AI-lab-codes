import copy
graph = [
    [8, 3, 4],
    [1, 7, 2],
    [5, 6, 0]]

#print(graph)
row_index = 0
col_index = 0
l = 3
n = 2
def up(graph):
    row_index = find_row_index(graph)
    col_index = find_col_index(graph)
    graph[row_index][col_index], graph[row_index-1][col_index] = graph[row_index-1][col_index], graph[row_index][col_index]
    print(graph)

def down(graph):
    row_index = find_row_index(graph)
    col_index = find_col_index(graph)
    graph[row_index][col_index], graph[row_index-1][col_index] = graph[row_index-1][col_index], graph[row_index][col_index]
    print(graph)

def left(graph):
    row_index = find_row_index(graph)
    col_index = find_col_index(graph)
    graph[row_index][col_index], graph[row_index-1][col_index] = graph[row_index-1][col_index], graph[row_index][col_index]
    print(graph)

def right(graph):
    row_index = find_row_index(graph)
    col_index = find_col_index(graph)
    graph[row_index][col_index], graph[row_index-1][col_index] = graph[row_index-1][col_index], graph[row_index][col_index]
    print(graph)

def find_row_index(matrix):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                return i
    return -1  # Return None if the target number is not found in the matrix

def find_col_index(matrix):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                return j
    return -1  # Return None if the target number is not found in the matrix

def create(graph,l):
    if l:
        row_index = find_row_index(graph)
        col_index = find_col_index(graph)
        print(graph)
        if row_index % n == 0 and col_index % n == 0:
            if row_index == n and col_index == n:
                dummy_graph = copy.deepcopy(graph)
                left(dummy_graph)
                create(dummy_graph,l-1)
                up(dummy_graph)
                create(dummy_graph,l-1)
            if row_index == 0 and col_index == 0:
                dummy_graph = copy.deepcopy(graph)
                right(dummy_graph)
                create(dummy_graph,l-1)
                down(dummy_graph)
                create(dummy_graph,l-1)
            if row_index != n and col_index == n:
                dummy_graph = copy.deepcopy(graph)
                left(dummy_graph)
                create(dummy_graph,l-1)
                down(dummy_graph)
                create(dummy_graph,l-1)
            if row_index == n and col_index != n:
                dummy_graph = copy.deepcopy(graph)
                right(dummy_graph)
                create(dummy_graph,l-1)
                up(dummy_graph)
                create(dummy_graph,l-1)
        else:
            print("Unknown condition")
            
        

create(graph,l)
