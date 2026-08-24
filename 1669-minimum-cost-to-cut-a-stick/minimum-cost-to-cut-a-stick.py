class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        m = len(cuts)
        dp = [[float('inf')]*m for _ in range(m)]
        for i in range(m-1):
            dp[i][i+1] = 0
        for length in range(2, m):
            for left in range(m - length):
                right = left + length
                for k in range(left+1, right):
                    dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + cuts[right] - cuts[left])
        return dp[0][m-1]