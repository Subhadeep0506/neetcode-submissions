class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_, col_ = [0] * len(matrix), [0] * len(matrix[0])
        row_len, col_len = len(matrix), len(matrix[0])

        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    row_[row], col_[col] = -1, -1
        
        for row in range(row_len):
            for col in range(col_len):
                if row_[row] == -1 or col_[col] == -1:
                    matrix[row][col] = 0