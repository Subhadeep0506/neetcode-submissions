class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        total = ROWS * COLS
        start, end = 0, total - 1
        while start <= end:
            mid = (start + end) // 2
            i = mid // COLS
            j = mid % COLS
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                end = mid - 1
            else:
                start = mid + 1
        return False