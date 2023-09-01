
l = 3 # no.of levels
m = 3
graph = [
    [1, 8, 3],
    [5, 7, 4],
    [6, 2, 0]
]
def up(graph,row_index,col_index):
    graph[row_index][col_index], graph[row_index-1][col_index] = graph[row_index-1][col_index], graph[row_index][col_index]

def down(graph,row_index,col_index):
    graph[row_index][col_index], graph[row_index+1][col_index] = graph[row_index+1][col_index], graph[row_index][col_index]

def left(graph,row_index,col_index):
    graph[row_index][col_index], graph[row_index][col_index-1] = graph[row_index][col_index-1], graph[row_index][col_index]

def right(graph,row_index,col_index):
    graph[row_index][col_index], graph[row_index][col_index+1] = graph[row_index][col_index+1], graph[row_index][col_index]

#print(graph)
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

def create(graph,next_row_index,next_col_index,l):
    if not l:
        return
    else:
        row_index, col_index = find_indices(graph) # type: ignore
        #print("Row and Col Index",row_index,col_index)
        c_next_row_index,c_next_col_index = next_row_index,next_col_index 
        #print("Next Row and Col Index",c_next_row_index,c_next_col_index)
        #swap_values(graph, row_index,col_index,next_row_index,next_col_index )
        
        graph[row_index][col_index], graph[c_next_row_index][c_next_col_index] = graph[c_next_row_index][c_next_col_index], graph[row_index][col_index]
        print(graph)
        #print("Swap Done!")
        #print("**************************************************************************")
        for i in range(4):
            if (row_index % 2 == 0 and col_index%2==0): # Corner
                #print(row_index,col_index)
                n = 2
            elif (row_index % 2 != 0 and col_index %2 == 0) or (row_index % 2 == 0 and col_index%2 !=0): # rest
                n = 3
            else : # Center
                n = 4  
    
        for i in range(n):
            if row_index ==2 and col_index == 2:
                indices = [[2,1],[1,2]]
                for j in indices:
                    create(graph,j[0],j[1],l-1)
            elif row_index ==0 and col_index == 0:
                indices = [[0,1],[1,0]]
                for j in indices:
                    create(graph,j[0],j[1],l-1)
            elif row_index == 0 and col_index == 2:
                indices = [[0,1],[1,2]]
                for j in indices:
                    create(graph,j[0],j[1],l-1)
            elif row_index == 2 and col_index == 0:
                indices = [[1,0],[2,1]]
                for j in indices:
                    create(graph,j[0],j[1],l-1)
            elif row_index == 1 and col_index == 1:
                indices = [[0,1],[1,2],[2,1],[1,0]]
                for j in indices:
                    create(graph,j[0],j[1],l-1)
            elif row_index == 0 and col_index == 1:
                indices = [[1,1],[0,0],[0,2]]
                for j in indices:
                    create(graph,j[0],j[1],l-1)
            elif row_index == 2 and col_index == 1:
                indices = [[2,2],[2,0],[1,1]]
                for j in indices:
                    create(graph,j[0],j[1],l-1)
            elif row_index == 1 and col_index == 0:
                indices = [[1,1],[0,0],[2,0]]
                for j in indices:
                    create(graph,j[0],j[1],l-1)
            elif row_index == 1 and col_index == 2:
                indices = [[1,1],[0,2],[2,2]]
                for j in indices:
                    create(graph,j[0],j[1],l-1)
            

            else:
                print("NOT MAINTAINED")
            
            
        

indices = find_indices(graph)
next_row_index,next_col_index = 2,2
create(graph,next_row_index,next_col_index,l) 