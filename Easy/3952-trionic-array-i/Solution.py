class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def is_increasing(arr):
            return all(arr[i]<arr[i+1] for i in range(len(arr)-1))

        def is_decreasing(arr):
            return all(arr[i]>arr[i+1] for i in range(len(arr)-1))

        for p in range(1, n-2): 
            if is_increasing(nums[:p+1]):
                for q in range(p+1, n-1):
                    if is_decreasing(nums[p:q+1]):
                        if is_increasing(nums[q:]):
                            return True
        return False