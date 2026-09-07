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
                # 1. Identify the mask of trailing ones.
                # Example: n = 23 (10111) -> n+1 = 24 (11000) -> XOR = 11111 -> Shift = 111
                trailing_ones_mask = (n ^ (n + 1)) >> 1
                
                # 2. Get the most significant bit (MSB) of that trailing block.
                # Example: mask = 7 (111) -> mask+1 = 8 (1000) -> Shift = 4 (100)
                msb_of_ones = (trailing_ones_mask + 1) >> 1
                
                # 3. Subtracting the MSB minimizes the result while satisfying the condition.
                ans.append(n - msb_of_ones)
                
        return ans