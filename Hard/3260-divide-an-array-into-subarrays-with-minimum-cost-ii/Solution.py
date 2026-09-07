import heapq

class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        base_cost = nums[0]
        
        target_k = k - 2
        
        small = [] 
        large = []
        
        small_sum = 0
        in_small = set()
        
        for idx in range(2, min(2 + dist, n)):
            val = nums[idx]
            
            heapq.heappush(small, (-val, idx))
            small_sum += val
            in_small.add(idx)
            
            val_neg, i_pop = heapq.heappop(small)
            small_sum -= (-val_neg)
            in_small.remove(i_pop)
            heapq.heappush(large, (-val_neg, i_pop))
            
            if len(in_small) < target_k:
                v_l, i_l = heapq.heappop(large)
                heapq.heappush(small, (-v_l, i_l))
                small_sum += v_l
                in_small.add(i_l)
                
        min_total = float('inf')
        
        for i1 in range(1, n - (k - 2)):
            if i1 > n - (k - 1):
                break
                
            current_total = base_cost + nums[i1] + small_sum
            if current_total < min_total:
                min_total = current_total
            
            out_idx = i1 + 1
            if out_idx < n:
                if out_idx in in_small:
                    small_sum -= nums[out_idx]
                    in_small.remove(out_idx)
            
            in_idx = i1 + 1 + dist
            if in_idx < n:
                val = nums[in_idx]
                
                heapq.heappush(small, (-val, in_idx))
                small_sum += val
                in_small.add(in_idx)
                
                while small and small[0][1] <= out_idx:
                    heapq.heappop(small)
                
                if small:
                    val_neg, i_pop = heapq.heappop(small)
                    small_sum -= (-val_neg)
                    in_small.remove(i_pop)
                    heapq.heappush(large, (-val_neg, i_pop))
            
            while len(in_small) < target_k:
                while large and large[0][1] <= out_idx:
                    heapq.heappop(large)
                
                if large:
                    v_l, i_l = heapq.heappop(large)
                    heapq.heappush(small, (-v_l, i_l))
                    small_sum += v_l
                    in_small.add(i_l)
                else:
                    break
                    
        return min_total