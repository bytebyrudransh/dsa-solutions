class Solution(object):
    def maximumAND(self, nums, k, m):
        ans = 0
        for b in range(30, -1, -1):
            cand = ans | (1 << b)
            costs = []
            for x in nums:
                t = x
                mask = cand & ~t
                while mask:
                    h = mask.bit_length() - 1
                    t = ((t >> h) + 1) << h
                    mask = cand & ~t
                costs.append(t - x)
            
            costs.sort()
            if sum(costs[:m]) <= k:
                ans = cand
        return ans