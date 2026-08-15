class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in mapping:
                return [mapping[remaining],i]
            mapping[nums[i]] = i