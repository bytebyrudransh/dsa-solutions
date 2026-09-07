class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        left=0
        right=k-1
        lowest=float('inf')
        print(nums)
        while right<len(nums):
            difference=nums[right]-nums[left]
            if difference<lowest:
                lowest=difference
            right+=1
            left+=1
        return lowest