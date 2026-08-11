class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def DFS(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == '0':
                return
            grid[row][col] = "0"
            for direction_row, direction_col in directions:
                DFS(row + direction_row, col + direction_col)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    DFS(row, col)
                    island_count += 1
        
        return island_count