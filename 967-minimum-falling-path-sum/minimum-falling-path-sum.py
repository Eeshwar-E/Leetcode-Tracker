class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0]
        for i in range(1,n):
            new_dp = [0]*n
            for j in range(n):
                new_dp[j] = matrix[i][j]
                if j < 1:
                    new_dp[j] += min(dp[j], dp[j+1])
                elif j == n - 1:
                    new_dp[j] += min(dp[j-1], dp[j])
                else:
                    new_dp[j] += min(dp[j-1], dp[j], dp[j+1])

            dp = new_dp
        return min(dp)