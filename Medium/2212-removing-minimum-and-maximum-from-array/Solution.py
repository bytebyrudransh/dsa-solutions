class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        i, j = min(min_idx, max_idx), max(min_idx, max_idx)

        option1 = j + 1
        
        option2 = n - i
        
        option3 = (i + 1) + (n - j)

        return min(option1, option2, option3)