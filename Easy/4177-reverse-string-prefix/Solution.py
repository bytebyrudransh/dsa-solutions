class Solution(object):
    def reversePrefix(self, s, k):
        x= s[:k]
        return x[::-1]+s[k:]
        