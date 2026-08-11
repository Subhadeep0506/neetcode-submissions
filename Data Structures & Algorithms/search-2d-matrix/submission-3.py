class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[ROWS - 1][COLS - 1]:
            return False

        row = 0
        top, bottom = row, ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        col = 0
        left, right = col, COLS - 1
        while left <= right:
            mid = (right + left) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
        return False