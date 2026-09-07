class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:
                mask = (n ^ (n + 1)) >> 1
                bit_to_remove = (mask + 1) >> 1
                ans.append(n - bit_to_remove)
                
        return ans