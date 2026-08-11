class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROW, COL = m, n
        dp = [[0 for _ in range(COL + 1)] for _ in range(ROW + 1)]
        dp[ROW-1][COL-1] = 1

        for i in range(ROW - 1, -1, -1):
            for j in range(COL -1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]