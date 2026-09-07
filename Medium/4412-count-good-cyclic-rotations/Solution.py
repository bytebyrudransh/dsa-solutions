class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n//2
        # sums calculation
        sum1 = sum(nums[:half])
        sum2 = sum(nums[half:])
        ans = 0 
        for i in range (n):
            if sum1 > sum2:
                ans += 1 

            remove_from_first = nums[i]
            added_to_first = nums[(i + half) % n]
            
            sum1 = sum1 - remove_from_first + added_to_first
            sum2 = sum2 - added_to_first + remove_from_first
        return ans     