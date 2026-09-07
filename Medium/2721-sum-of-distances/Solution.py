from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        # Step 1: group indices
        groups = defaultdict(list)
        for i, val in enumerate(nums):
            groups[val].append(i)
        
        # Step 2: process each group
        for pos in groups.values():
            k = len(pos)
            
            # prefix sum
            prefix = [0] * k
            prefix[0] = pos[0]
            for i in range(1, k):
                prefix[i] = prefix[i-1] + pos[i]
            
            for j in range(k):
                idx = pos[j]
                
                # left contribution
                if j > 0:
                    left = j * pos[j] - prefix[j-1]
                else:
                    left = 0
                
                # right contribution
                if j < k - 1:
                    right = (prefix[k-1] - prefix[j]) - (k - j - 1) * pos[j]
                else:
                    right = 0
                
                res[idx] = left + right
        
        return res