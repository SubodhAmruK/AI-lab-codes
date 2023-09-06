import copy

n = 2
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

def print_graph(graph):
    for row in graph:
        for col in row:
            print(col, end=" ")
        print()
    print()

def main():
    
    graph = [[8, 3, 4], [1, 7, 2], [5, 6, 0]]
    cgraph = []
    cgraph.append(copy.deepcopy(graph))
    print_graph(graph)
    i=1
    while i<=10:
        print("Level " + str(i))
        graph = cgraph.pop(0)
        row_index = find_row_index(graph)
        col_index = find_col_index(graph)
        
        if up(graph, row_index, col_index):
            temp = graph[row_index][col_index]
            graph[row_index][col_index] = graph[row_index - 1][col_index]
            graph[row_index - 1][col_index] = temp
            print_graph(graph)
            cgraph.append(copy.deepcopy(graph))
            temp = graph[row_index][col_index]
            graph[row_index][col_index] = graph[row_index - 1][col_index]
            graph[row_index - 1][col_index] = temp

        if down(graph, row_index, col_index):
            temp = graph[row_index][col_index]
            graph[row_index][col_index] = graph[row_index + 1][col_index]
            graph[row_index + 1][col_index] = temp
            print_graph(graph)
            cgraph.append(copy.deepcopy(graph))
            temp = graph[row_index][col_index]
            graph[row_index][col_index] = graph[row_index + 1][col_index]
            graph[row_index + 1][col_index] = temp

        if right(graph, row_index, col_index):
            temp = graph[row_index][col_index]
            graph[row_index][col_index] = graph[row_index][col_index + 1]
            graph[row_index][col_index + 1] = temp
            print_graph(graph)
            cgraph.append(copy.deepcopy(graph))
            temp = graph[row_index][col_index]
            graph[row_index][col_index] = graph[row_index][col_index + 1]
            graph[row_index][col_index + 1] = temp

        if left(graph, row_index, col_index):
            temp = graph[row_index][col_index]
            graph[row_index][col_index] = graph[row_index][col_index - 1]
            graph[row_index][col_index - 1] = temp
            print_graph(graph)
            cgraph.append(copy.deepcopy(graph))
            temp = graph[row_index][col_index]
            graph[row_index][col_index] = graph[row_index][col_index - 1]
            graph[row_index][col_index - 1] = temp
        i+=1

if __name__ == "__main__":
    main()
