# trying to make code faster

class Solution(object):
    def stoneGameVIII(self, stones):
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]
            
        ans = stones[-1]
        for i in range(len(stones) - 3, -1, -1):
            val = stones[i + 1] - ans
            if val > ans:
                ans = val
                
        return ans