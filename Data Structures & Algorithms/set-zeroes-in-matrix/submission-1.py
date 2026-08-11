class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        _temp = [row[:] for row in matrix]
        row_len, col_len = len(matrix), len(matrix[0])
        
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    for _col in range(col_len):
                        if matrix[row][_col] != 0:
                            matrix[row][_col] = -1
                    for _row in range(row_len):
                        if matrix[_row][col] != 0:
                            matrix[_row][col] = -1
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == -1:
                    matrix[row][col] = 0