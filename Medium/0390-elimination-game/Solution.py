class Solution:
    def lastRemaining(self, n):
        ans = 1
        step = 1
        left = True

        while n > 1:
            if left or n % 2:
                ans += step
            step *= 2
            n //= 2
            left = not left

        return ans