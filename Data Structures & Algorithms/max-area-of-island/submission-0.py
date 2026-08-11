class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def DFS(row, col, area):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
                return area
            area += 1
            grid[row][col] = 0
            for dir_row, dir_col in directions:
                area = DFS(row + dir_row, col + dir_col, area)
            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    curr_area = 0
                    curr_area = DFS(row, col, curr_area)
                    max_area = max(curr_area, max_area)
        
        return max_area
                