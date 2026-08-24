class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k-1) != 0:
            return -1
        
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1]+x)
        
        dp = [[0]*n for _ in range(n)]
        for length in range(2, n+1):
            for left in range(n - length + 1):
                right = left + length - 1
                dp[left][right] = float("inf")
                for mid in range(left, right, k-1):
                    dp[left][right] = min(dp[left][right], dp[left][mid] + dp[mid+1][right])

                if (right- left) % (k-1) == 0:
                    dp[left][right] += prefix[right+1] - prefix[left]
        
        return dp[0][n-1]
