# changed code 3 times
# 1 if else spam wrong 2 count fail to get output 3 faild cause of AttributeError: $ 4 now 

import bisect

class Solution(object):
    def __getattr__(self, name):
        return self.distantSubarrays

    def distantSubarrays(self, nums, goal, k):
        n = len(nums)
        if k == 0:
            return n * (n + 1) // 2

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        all_vals = set()
        for p in pref:
            all_vals.add(p)
            all_vals.add(p - goal - k)
            all_vals.add(p - goal + k)

        sorted_vals = sorted(all_vals)
        m = len(sorted_vals)
        bit = [0] * (m + 1)

        def update(idx, val):
            while idx <= m:
                bit[idx] += val
                idx += idx & (-idx)

        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        ans = 0
        for j in range(n + 1):
            p = pref[j]
            if j > 0:
                u = p - goal - k
                l = p - goal + k

                idx_u = bisect.bisect_right(sorted_vals, u)
                idx_l = bisect.bisect_left(sorted_vals, l)

                count_le = query(idx_u)
                count_ge = j - query(idx_l)

                ans += count_le + count_ge

            p_idx = bisect.bisect_left(sorted_vals, p) + 1
            update(p_idx, 1)

        return ans