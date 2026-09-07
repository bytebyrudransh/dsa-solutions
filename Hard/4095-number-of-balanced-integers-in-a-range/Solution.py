class Solution(object):
    def countBalanced(self, low, high):
        def count_upto(n):
            if n <= 0: return 0
            s = str(n)
            memo = {}

            def dp(pos, is_less, is_started, diff):
                state = (pos, is_less, is_started, diff)
                if pos == len(s):
                    return 1 if (is_started and diff == 0) else 0
                if state in memo:
                    return memo[state]

                res = 0
                limit = int(s[pos]) if not is_less else 9
                
                for d in range(limit + 1):
                    next_less = is_less or (d < limit)
                    next_started = is_started or (d > 0)
                    
                    next_diff = diff
                    if next_started:
                        # Odd-indexed digits (1st, 3rd...) add, Even-indexed (2nd, 4th...) subtract
                        if pos % 2 == 0:
                            next_diff += d
                        else:
                            next_diff -= d
                    
                    res += dp(pos + 1, next_less, next_started, next_diff)
                
                memo[state] = res
                return res

            return dp(0, False, False, 0)

        return count_upto(high) - count_upto(low - 1)