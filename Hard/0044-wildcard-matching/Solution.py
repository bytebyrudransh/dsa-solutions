class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        prev = [False] * (n + 1)
        prev[0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]
            else:
                break
        
        for i in range(1, m + 1):
            curr = [False] * (n + 1)
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    curr[j] = curr[j - 1] or prev[j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    curr[j] = prev[j - 1]
            prev = curr
        
        return prev[n]