class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            n1=nums[i]
            index=i+1
            while index<len(nums):
                n2=nums[index]
                if n1+n2==target:
                    return i,index
                index+=1