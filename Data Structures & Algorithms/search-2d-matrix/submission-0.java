class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // search row and first column for the number / row to search through
        int rowFirstPtr = 0;
        int rowEndPtr = matrix.length - 1;
        int n = matrix[0].length;
        while (rowFirstPtr < rowEndPtr) {
            int rowMid = (rowFirstPtr + rowEndPtr + 1) / 2;
            if (matrix[rowMid][0] == target) {
                return true;
            }

            if (matrix[rowMid][0] < target) {
                rowFirstPtr = rowMid;
            } else if (matrix[rowMid][0] > target) {
                rowEndPtr = rowMid - 1;
            }
        }
        // houses the row that should hold the target
        int rowPtr = rowFirstPtr;
        
        // we should have the row from rowEndPtr or rowFirstPtr
        int colFirstPtr = 0;
        int colEndPtr = matrix[rowPtr].length - 1;
        while (colFirstPtr <= colEndPtr) {
            int colMid = (colFirstPtr + colEndPtr) / 2;
            if (matrix[rowPtr][colMid] == target) {
                return true;
            }
            if (matrix[rowPtr][colMid] < target) {
                colFirstPtr = colMid + 1;
            } else if (matrix[rowPtr][colMid] > target) {
                colEndPtr = colMid - 1;
            }
        }
        return false;
    }
}
