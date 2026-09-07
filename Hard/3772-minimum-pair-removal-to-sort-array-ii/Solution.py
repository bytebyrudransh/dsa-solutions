import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        
        vals = list(nums)
        prev = list(range(-1, n - 1))
        next_ = list(range(1, n + 1))
        heap = []
        descents = 0
        removed = [False] * n 

        for i in range(n - 1):
            s = vals[i] + vals[i+1]
            heapq.heappush(heap, (s, i))
            if vals[i] > vals[i+1]:
                descents += 1
                
        ops = 0
        
        while descents > 0:
            while True:
                s, i = heapq.heappop(heap)
                j = next_[i]
                if not removed[i] and j < n and not removed[j] and s == vals[i] + vals[j]:
                    break
            
            if i > 0:
                p = prev[i]
                if p != -1 and vals[p] > vals[i]:
                    descents -= 1
            
            if vals[i] > vals[j]:
                descents -= 1
                
            k = next_[j]
            if k < n:
                if vals[j] > vals[k]:
                    descents -= 1
            
            vals[i] += vals[j]
            removed[j] = True
            
            next_[i] = k
            if k < n:
                prev[k] = i
            
            if i > 0:
                p = prev[i]
                if p != -1 and vals[p] > vals[i]:
                    descents += 1
            
            if k < n:
                if vals[i] > vals[k]:
                    descents += 1
            
            if k < n:
                heapq.heappush(heap, (vals[i] + vals[k], i))
                
            if prev[i] != -1:
                p = prev[i]
                heapq.heappush(heap, (vals[p] + vals[i], p))

            ops += 1
            
        return ops
