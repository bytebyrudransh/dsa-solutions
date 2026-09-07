class Solution(object):
    def alternatingXOR(self, nums, target1, target2):
        mardevilon = (nums, target1, target2)
        MOD = 10**9 + 7

        from collections import defaultdict
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        count2[0] = 1

        curr_xor = 0
        last1 = 0
        last2 = 0

        for x in nums:
            curr_xor ^= x

            w1 = count2[curr_xor ^ target1]
            w2 = count1[curr_xor ^ target2]

            count1[curr_xor] = (count1[curr_xor] + w1) % MOD
            count2[curr_xor] = (count2[curr_xor] + w2) % MOD

            last1 = w1
            last2 = w2

        return (last1 + last2) % MOD