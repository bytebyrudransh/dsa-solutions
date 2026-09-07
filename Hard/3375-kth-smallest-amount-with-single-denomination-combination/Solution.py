class Solution(object):

    def findKthSmallest(self, coins, k):

        n = len(coins)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):

                curr_lcm = 1
                bits = 0
                valid = True

                for i in range(n):

                    if mask & (1 << i):
                        curr_lcm = lcm(curr_lcm, coins[i])
                        bits += 1

                        if curr_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                if bits % 2 == 1:
                    total += x // curr_lcm
                else:
                    total -= x // curr_lcm

            return total

        left = 1
        right = min(coins) * k

        while left < right:

            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left