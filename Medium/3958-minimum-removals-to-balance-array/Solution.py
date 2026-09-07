class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        
        n = len(nums)
        left = 0
        max_len = 0
        
        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                
        return n - max_len