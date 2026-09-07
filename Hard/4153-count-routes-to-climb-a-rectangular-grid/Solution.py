#trying to low run time 
class Solution(object):
    def numberOfRoutes(self, grid, d):
        MOD = 10**9 + 7
        n = len(grid)
        m = len(grid[0])

        if d > 1:
            max_dist_v = int((d * d - 1) ** 0.5)
        else:
            max_dist_v = 0

        dp_v = [0] * m
        dp_h = [0] * m

        for c in range(m):
            if grid[n - 1][c] == '.':
                dp_v[c] = 1

        prefix = [0] * (m + 1)
        acc = 0
        for c in range(m):
            acc = (acc + dp_v[c]) % MOD
            prefix[c + 1] = acc

        for c in range(m):
            if grid[n - 1][c] == '.':
                r = min(m, c + d + 1)
                l = max(0, c - d)
                dp_h[c] = (prefix[r] - prefix[l] - dp_v[c]) % MOD

        for r in range(n - 2, -1, -1):
            acc = 0
            for c in range(m):
                acc = (acc + dp_v[c] + dp_h[c]) % MOD
                prefix[c + 1] = acc

            new_dp_v = [0] * m
            for c in range(m):
                if grid[r][c] == '.':
                    rr = min(m, c + max_dist_v + 1)
                    ll = max(0, c - max_dist_v)
                    new_dp_v[c] = (prefix[rr] - prefix[ll]) % MOD

            acc = 0
            for c in range(m):
                acc = (acc + new_dp_v[c]) % MOD
                prefix[c + 1] = acc

            new_dp_h = [0] * m
            for c in range(m):
                if grid[r][c] == '.':
                    rr = min(m, c + d + 1)
                    ll = max(0, c - d)
                    new_dp_h[c] = (prefix[rr] - prefix[ll] - new_dp_v[c]) % MOD

            dp_v = new_dp_v
            dp_h = new_dp_h

        return (sum(dp_v) + sum(dp_h)) % MOD