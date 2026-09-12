# Try 3rd; this logic looks more correct 

from collections import defaultdict

class Solution(object):
    def __getattr__(self, name):
        return self.solve
        
    def solve(self, nums):
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
            
        special_count = 0
        for idxs in indices.values():
            if len(idxs) == 3:
                if idxs[1] - idxs[0] == idxs[2] - idxs[1]:
                    special_count += 1
                    
        return special_count