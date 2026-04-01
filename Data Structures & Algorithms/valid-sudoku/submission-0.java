class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            if (!checkRow(board, i)) return false;
            for (int j = 0; j < 9; j++) {
                if (!checkColumn(board, j)) return false;
                // check box at top left of square.
                if (j % 3 == 0 && i % 3 == 0) {
                    if (!checkBox(board, i, j)) return false;
                }
            }
        }
        return true;
    }

    // check for duplicates inside 3x3 box
    public boolean checkBox(char[][] board, int row, int col) {
        Set<Character> seenBox = new HashSet<>(); 
        // rows
        for (int i = row; i < row + 3; i++) {
            for (int j = col; j < col + 3; j++) {
                if (seenBox.contains(board[i][j]) && board[i][j] != '.') {
                    System.out.println("box has duplicate");
                    return false;
                }
                seenBox.add(board[i][j]);
            }
        }
        return true;
    }

    // check given row for duplicates
    public boolean checkRow(char[][] board, int row) {
        Set<Character> seenRow = new HashSet<>();
        for (int i = 0; i < board.length - 1; i++) {
            if (seenRow.contains(board[row][i]) && board[row][i] != '.') {
                System.out.println("row has duplicate");
                return false;
            }
            seenRow.add(board[row][i]);
        }
        return true;
    }

    // check given column for duplicates
    public boolean checkColumn(char[][] board, int col) {
        Set<Character> seenCol = new HashSet<>(); 
        for (int i = 0; i < board[i].length - 1; i++) {
            if (seenCol.contains(board[i][col]) && board[i][col] != '.') {
                System.out.println("col has duplicate");
                return false;
            }
            seenCol.add(board[i][col]);
        }
        return true;
    }
}
