class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)
        #dp = [0]*(n+1)
        count = 1
        end = pairs[0][1]
        for i in range(1, n):
            if end < pairs[i][0]:
                end = pairs[i][1]
                count += 1
            else:
                continue
        return count