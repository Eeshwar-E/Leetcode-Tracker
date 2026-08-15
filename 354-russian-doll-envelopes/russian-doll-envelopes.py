class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        count = 1
        heights = []
        for _, height in envelopes:
            heights.append(height)
        
        tails = []
        for height in heights:
            if len(tails) == 0:
                tails.append(height)
                continue
            left = 0
            right = len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] >= height:
                    right = mid
                else:
                    left = mid + 1
            pos = left
            if pos == len(tails):
                tails.append(height)
            else:
                tails[pos] = height
        return len(tails)