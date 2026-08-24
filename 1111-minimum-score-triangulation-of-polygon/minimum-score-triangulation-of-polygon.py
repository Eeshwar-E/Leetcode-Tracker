class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        if len(values) < 3:
            return 0
        n = len(values)
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            if i + 1 < n:
                dp[i][i+1] = 0
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (values[i]*values[j]*values[k]))
        
        return dp[0][n-1]
                