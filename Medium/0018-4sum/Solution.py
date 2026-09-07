class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 3):
            # Skip duplicate first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicate second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two-pointer search for the remaining pair
                left, right = j + 1, n - 1
                needed = target - nums[i] - nums[j]
                
                while left < right:
                    s = nums[left] + nums[right]
                    if s == needed:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates on both sides
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < needed:
                        left += 1
                    else:
                        right -= 1
        
        return result