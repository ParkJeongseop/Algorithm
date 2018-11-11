
public class OopEx6RowColSum {

  public static void main(String[] args) {
    int[][] matrix = {{40, 70, 100}, {32, 14, 53}};
    int row = matrix.length;
    int col = matrix[0].length;
    int[] answer = new int[row + col+1];
    for (int r = 0; r < row; r++) {
      for (int c = 0; c < col; c++) {
        answer[r] += matrix[r][c];
        answer[row + c] += matrix[r][c];
        answer[row + col] += matrix[r][c];
      }
    }
    
    for(int i : answer) {
      System.out.print(i + ", ");
    }
    
  }

  public static int[] Solution(int[][] matrix) {
    int row = matrix.length;
    int col = matrix[0].length;
    int[] answer = new int[row + col+1];
    for (int r = 0; r < row; r++) {
      for (int c = 0; c < col; c++) {
        answer[r] += matrix[r][c];
        answer[row + c] += matrix[r][c];
        answer[row + col] += matrix[r][c];
      }
    }
    return answer;
  }

}
