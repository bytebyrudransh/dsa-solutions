class Solution:
    def minimumCost(self, nums):
        n = len(nums)
        min_sum = float('inf')
        
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                current_sum = nums[0] + nums[i] + nums[j]
                if current_sum < min_sum:
                    min_sum = current_sum
                    
        return min_sum