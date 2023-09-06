import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;

public class Main{
    int l = 0;
    static int n=2;
    static int[][] Mgraph = {
            {8, 3, 4},
            {1, 7, 2},
            {5, 6, 0}
    };

    static boolean up(int[][] graph, int row_index, int col_index) {
        //int row_index = findRowIndex(graph);
        //int col_index = findColIndex(graph);
        //int temp = graph[row_index][col_index];
        //graph[row_index][col_index] = graph[row_index - 1][col_index];
        //graph[row_index - 1][col_index] = temp;
        //printGraph(graph);
        if (row_index - 1 >= 0) {
            return true;
        }
        return false;
    }

    static boolean down(int[][] graph, int row_index, int col_index) {
        //int row_index = findRowIndex(graph);
        //int col_index = findColIndex(graph);
        //int temp = graph[row_index][col_index];
        //graph[row_index][col_index] = graph[row_index + 1][col_index];
        //graph[row_index + 1][col_index] = temp;
        //printGraph(graph);
        if (row_index + 1 <= n) {
            return true;
        }
        return false;
    }

    static boolean left(int[][] graph, int row_index, int col_index) {
        /*int row_index = findRowIndex(graph);
        int col_index = findColIndex(graph);
        int temp = graph[row_index][col_index];
        graph[row_index][col_index] = graph[row_index][col_index - 1];
        graph[row_index][col_index - 1] = temp;
        printGraph(graph);*/
        if (col_index - 1 >= 0) {
            return true;
        }
        return false;
    }

    static boolean right(int[][] graph, int row_index, int col_index) {
        //int row_index = findRowIndex(graph);
        //int col_index = findColIndex(graph);
        //int temp = graph[row_index][col_index];
        //graph[row_index][col_index] = graph[row_index][col_index + 1];
        //graph[row_index][col_index + 1] = temp;
        //printGraph(graph);
        if (col_index + 1 <= n) {
            return true;
        }
        return false;
    }

    static int findRowIndex(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    return i;
                }
            }
        }
        return -1;
    }

    static int findColIndex(int[][] matrix) {
        for (int[] ints : matrix) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (ints[j] == 0) {
                    return j;
                }
            }
        }
        return -1;
    }

    static void printGraph(int[][] graph) {
        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph[0].length; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
    public static void main(String[] args) {
        //PTrees[] t = new PTrees[20];
        //PTrees t1 = new PTrees();
        Queue<int[][]> cgraph = new LinkedList<>();
        cgraph.offer(deepCopy(Mgraph));
        printGraph(Mgraph);
        for(int i=0;i<3;i++)
        {
            System.out.println("Level "+(i+1));
            int[][] graph = cgraph.poll();
            //printGraph(graph);
            int row_index = findRowIndex(graph);
            int col_index = findColIndex(graph);
            if (up(graph, row_index,col_index))
            {
                int temp = graph[row_index][col_index];
                graph[row_index][col_index] = graph[row_index - 1][col_index];
                graph[row_index - 1][col_index] = temp;
                printGraph(graph);
                cgraph.offer(deepCopy(graph));
                printGraph(graph);
                temp = graph[row_index][col_index];
                graph[row_index][col_index] = graph[row_index - 1][col_index];
                graph[row_index - 1][col_index] = temp;
            }
            if (down(graph,row_index,col_index)) {
                int temp = graph[row_index][col_index];
                graph[row_index][col_index] = graph[row_index+1][col_index];
                graph[row_index+1][col_index] = temp;
                cgraph.offer(deepCopy(graph));
                printGraph(graph);
                temp = graph[row_index][col_index];
                graph[row_index][col_index] = graph[row_index+1][col_index];
                graph[row_index+1][col_index] = temp;
            }
            if (right(graph,row_index,col_index)) {
                int temp = graph[row_index][col_index];
                graph[row_index][col_index] = graph[row_index][col_index + 1];
                graph[row_index][col_index + 1] = temp;
                cgraph.offer(deepCopy(graph));
                printGraph(graph);
                temp = graph[row_index][col_index];
                graph[row_index][col_index] = graph[row_index][col_index + 1];
                graph[row_index][col_index + 1] = temp;
            }

            if (left(graph,row_index,col_index)) {
                int temp = graph[row_index][col_index];
                graph[row_index][col_index] = graph[row_index][col_index - 1];
                graph[row_index][col_index - 1] = temp;
                cgraph.offer(deepCopy(graph));
                printGraph(graph);
                temp = graph[row_index][col_index];
                graph[row_index][col_index] = graph[row_index][col_index - 1];
                graph[row_index][col_index - 1] = temp;
            }
        }
    }
}
