class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        max_pair_sum = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum > max_pair_sum:
                max_pair_sum = current_sum
            left += 1
            right -= 1
            
        return max_pair_sum