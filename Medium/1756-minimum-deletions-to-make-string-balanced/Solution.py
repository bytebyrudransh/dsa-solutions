class Solution:
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        b_count = 0
        min_deletions = 0
        
        for char in s:
            if char == 'b':
                b_count += 1
            else:
                
                min_deletions = min(min_deletions + 1, b_count)
                
        return min_deletions