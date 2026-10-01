class Solution:
    

    def solveNQueens(self, n: int) -> List[List[str]]:
        # choices: put down n queens on an nxn board.
        # constraints: queen cannot be in the diagonal, or in the row or column of another queen. 
        # base case: number of queens put down is the same as n
        # backtracking step: pop (i, j)-th position?
        res = []
        board = [['.'] * n for _ in range(n)]
        
        def isSafe(r: int, c: int):
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1

            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = r - 1, c + 1
            while row >= 0 and col < len(board):
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if not isSafe(row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

        # convert board into strings
        backtrack(0)
        print(res)
        return res