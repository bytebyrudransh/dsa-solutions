class Solution(object):
    def minLength(self, nums, k):
        from collections import defaultdict

        counts = defaultdict(int)
        current_sum = 0
        left = 0
        min_len = float('inf')

        for right, num in enumerate(nums):
            if counts[num] == 0:
                current_sum += num
            counts[num] += 1

            while current_sum >= k:
                min_len = min(min_len, right - left + 1)
                remove_num = nums[left]
                counts[remove_num] -= 1
                if counts[remove_num] == 0:
                    current_sum -= remove_num
                left += 1

        return min_len if min_len != float('inf') else -1