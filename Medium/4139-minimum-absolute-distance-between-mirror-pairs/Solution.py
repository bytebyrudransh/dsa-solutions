from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen = {}
        min_dist = float('inf')
        
        for i, val in enumerate(nums):
            if val in last_seen:
                min_dist = min(min_dist, i - last_seen[val])
            
            rev_val = int(str(val)[::-1])
            last_seen[rev_val] = i
            
        return min_dist if min_dist != float('inf') else -1