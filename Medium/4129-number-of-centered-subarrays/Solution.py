class Solution(object):
    def centeredSubarrays(self, nums):
        count = 0
        n = len(nums)

        # Iterate through all possible starting points of subarrays
        for i in range(n):
            total = 0
            seen = set()
            # Iterate through all ending points
            for j in range(i, n):
                total += nums[j]
                seen.add(nums[j])
                
                # Check if the current subarray sum exists in the elements seen so far
                if total in seen:
                    count += 1

        return count