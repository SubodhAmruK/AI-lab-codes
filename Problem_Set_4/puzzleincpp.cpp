#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph = {
    {8, 3, 4},
    {1, 7, 2},
    {5, 6, 0}
};

vector<vector<int>> dummy_graph = {
    {8, 3, 4},
    {1, 7, 2},
    {5, 6, 0}
};

void up(int row_index, int col_index) {
    /*cout << "Graph ";
    for (const auto& row : graph) {
        for (int value : row) {
            cout << value << " ";
        }
    }
    cout << endl;

    cout << "Dummy Graph ";
    for (const auto& row : dummy_graph) {
        for (int value : row) {
            cout << value << " ";
        }
    }
    cout << endl;*/
    dummy_graph = graph;
    swap(dummy_graph[row_index][col_index], dummy_graph[row_index - 1][col_index]);
    
    //cout << "Dummy Graph after 'up': ";
    for (const auto& row : dummy_graph) {
        for (int value : row) {
            cout <<value << " ";
        }
    }
    cout << endl;
}

void down(int row_index, int col_index) {
    swap(dummy_graph[row_index][col_index], dummy_graph[row_index + 1][col_index]);
    
    cout << "Dummy Graph after 'down': ";
    for (const auto& row : dummy_graph) {
        for (int value : row) {
            cout << value << " ";
        }
    }
    cout << endl;
}

void left(int row_index, int col_index) {
    /*cout << "Graph ";
    for (const auto& row : graph) {
        for (int value : row) {
            cout << value << " ";
        }
    }
    cout << endl;

    cout << "Dummy Graph ";
    for (const auto& row : dummy_graph) {
        for (int value : row) {
            cout << value << " ";
        }
    }
    cout << endl;*/

    swap(dummy_graph[row_index][col_index], dummy_graph[row_index][col_index - 1]);
    
    //cout << "Dummy Graph after 'left': ";
    for (const auto& row : dummy_graph) {
        for (int value : row) {
            cout << value << " ";
        }
    }
    cout << endl;
}

void right(int row_index, int col_index) {
    swap(dummy_graph[row_index][col_index], dummy_graph[row_index][col_index + 1]);
    
    cout << "Dummy Graph after 'right': ";
    for (const auto& row : dummy_graph) {
        for (int value : row) {
            cout << value << " ";
        }
    }
    cout << endl;
}

int find_row_index() {
    for (int i = 0; i < graph.size(); i++) {
        for (int j = 0; j < graph[i].size(); j++) {
            if (graph[i][j] == 0) {
                return i;
            }
        }
    }
    return -1;  // Return -1 if the target number is not found in the matrix
}

int find_col_index() {
    for (int i = 0; i < graph.size(); i++) {
        for (int j = 0; j < graph[i].size(); j++) {
            if (graph[i][j] == 0) {
                return j;
            }
        }
    }
    return -1;  // Return -1 if the target number is not found in the matrix
}

int l = 3;
int n = 2;

void create(int l) {
    if (l == 0) {
        return;
    }
    int row = find_row_index();
    int col = find_col_index();
    if (row == n && col == n) {
        cout << "at 2,2" << endl;
        left(row, col);
        create(l-1);
        up(row, col);
        create(l-1);
    } else if (row == 0 && col == 0) {
        cout << "at 0,0" << endl;
        right(row, col);
        create(l-1);
        down(row, col);
        create(l-1);
    } else if (row == 0 && col == n) {
        cout << "at 0," << n << endl;
        left(row, col);
        create(l-1);
        down(row, col);
        create(l-1);
    } else if (row == n && col == 0) {
        cout << "at " << n << ",0" << endl;
        right(row, col);
        create(l-1);
        up(row, col);
        create(l-1);
    } else if (row == 0 && col % n != 0) {
        cout << "at 0,1 or 0,2" << endl;
        left(row, col);
        create(l-1);
        right(row, col);
        create(l-1);
        down(row, col);
        create(l-1);
    } else if (row % n != 0 && col == 0) {
        cout << "at 1,0 or 2,0" << endl;
        right(row, col);
        create(l-1);
        up(row, col);
        create(l-1);
        down(row, col);
        create(l-1);
    } else if (row == n && col % n != 0) {
        cout << "at " << n << ",1" << endl;
        right(row, col);
        create(l-1);
        left(row, col);
        create(l-1);
        up(row, col);
        create(l-1);
    } else if (row % n != 0 && col == n) {
        cout << "at 1," << n << endl;
        left(row, col);
        create(l-1);
        up(row, col);
        create(l-1);
        down(row, col);
        create(l-1);
    } else if (row % n != 0 && col % n != 0) {
        cout << "at 1,1" << endl;
        up(row, col);
        create(l-1);
        down(row, col);
        create(l-1);
        left(row, col);
        create(l-1);
        right(row, col);
        create(l-1);
    } else {
        cout << "No condition matched!" << endl;
    }
}

int main() {
    create(l);
    return 0;
}
