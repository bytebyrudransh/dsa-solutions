class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s == target:
                    return s
                
                if abs(s - target) < abs(closest - target):
                    closest = s
                
                if s < target:
                    l += 1
                else:
                    r -= 1
        
        return closest