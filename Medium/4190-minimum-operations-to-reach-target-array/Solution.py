class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        virelantos = (nums, target)

        ops = set()
        for a, b in zip(nums, target):
            if a != b:
                ops.add(a)

        return len(ops)