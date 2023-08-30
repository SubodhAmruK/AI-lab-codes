
l = 3 # no.of levels
graph = [
    [1, 8, 3],
    [5, 7, 4],
    [6, 2, 0]
]

print(graph)
def find_indices(matrix):
    for row_index, row in enumerate(matrix):
        try:
            col_index = row.index(0)
            return row_index, col_index
        except ValueError:
            pass
    return None  # Return None if the target number is not found in the matrix

def swap_values(matrix, row1, col1, row2, col2):
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

n = 0 # no.of moves

def create(graph,indices):
    row_index, col_index = find_indices(graph) # type: ignore
    next_row_index,next_col_index = indices 
    #swap_values(graph, row_index,col_index,next_row_index,next_col_index )
    
    graph[row_index][col_index], graph[next_row_index][next_col_index] = graph[next_row_index][next_col_index], graph[row_index][col_index]
    print(graph)
    for i in range(4):
        if (row_index % 2 == 0 and col_index%2==0): # Corner
            #print(row_index,col_index)
            n = 2
        elif (row_index % 2 != 0 and col_index %2 == 0) or (row_index % 2 == 0 and col_index%2 !=0): # rest
            n=3
        else : # Center
            n = 4  
  
    for i in range(n):
        if row_index ==2 and col_index == 2:
            indices = ((1,2),(2,1))
            for j in indices[i]:
                create(graph,j)
        

indices = find_indices(graph)
next_row_index,next_col_index = 0,0
create(graph,indices) 