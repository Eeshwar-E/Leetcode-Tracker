class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_size = 0
        if matrix[0][0] == "1":
            dp[1][1] = 1
            max_size += 1
        for i in range(m+1):
            dp[i][0] = 0
        for j in range(n+1):
            dp[0][j] = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    max_size = max(max_size, dp[i][j]**2)
        return max_size
