class Solution(object):
    def minimumPairRemoval(self, nums):
        a = 0
        while nums != sorted(nums) and len(nums) > 1:
            mn = min(nums[i] + nums[i + 1] for i in range(len(nums) - 1))
            for i in range(len(nums) - 1):
                if (nums[i] + nums[i + 1]) == mn:
                    nums.pop(i)
                    nums[i] = mn
                    break
            a += 1
        return a
        