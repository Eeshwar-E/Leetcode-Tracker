class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        count = [1]*n
        current_length = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    current_length = dp[j] + 1
                    if current_length > dp[i]:
                        count[i] = count[j]
                        dp[i] = dp[j] + 1
                    elif current_length == dp[i]:
                        count[i] += count[j]
        result = 0
        maxval = max(dp)
        for i in range(n):
            if dp[i] == maxval:
                result += count[i]
        return result