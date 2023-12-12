public class searchMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        int i = 0;
        int j = matrix.length -1;
        while (j >= 0 && i < matrix[0].length) {
            if (matrix[j][i] == target) {
                return true;
            } else if (matrix[j][i] > target) {
                j--;
            } else {
                i++;
            }
        }
        return false;
    }
}
