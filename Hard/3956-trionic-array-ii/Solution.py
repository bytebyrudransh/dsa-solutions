class Solution(object):
    def maxSumTrionic(self, nums):
        n = len(nums)
        
        INF = float('inf')
        dp1 = -INF  
        dp2 = -INF  
        dp3 = -INF 
        
        ans = -INF
        
        for i in range(1, n):
            curr = nums[i]
            prev = nums[i-1]
            
            new_dp1 = -INF
            new_dp2 = -INF
            new_dp3 = -INF
            
            if curr > prev:
                if dp1 != -INF:
                    new_dp1 = max(dp1 + curr, prev + curr)
                else:
                    new_dp1 = prev + curr
                
                candidates = []
                if dp3 != -INF:
                    candidates.append(dp3 + curr)
                if dp2 != -INF:
                    candidates.append(dp2 + curr)
                
                if candidates:
                    new_dp3 = max(candidates)
                    
            elif curr < prev:
                candidates = []
                if dp2 != -INF:
                    candidates.append(dp2 + curr)
                if dp1 != -INF:
                    candidates.append(dp1 + curr)
                
                if candidates:
                    new_dp2 = max(candidates)
            
            dp1, dp2, dp3 = new_dp1, new_dp2, new_dp3
            
            if dp3 > ans:
                ans = dp3
                
        return ans