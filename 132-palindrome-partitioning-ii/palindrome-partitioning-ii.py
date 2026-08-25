class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        n = len(s)
        pal = [[False]*n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True

        for i in range(1, n):
            for j in range(i+1):
                if s[i] == s[j]:
                    if i - j <= 2:
                        pal[j][i] = True
                    else:
                        pal[j][i] = pal[j+1][i-1]
        
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i+1):
                if pal[j][i]:
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], 1 + dp[j-1])
        
        return dp[n-1]
        