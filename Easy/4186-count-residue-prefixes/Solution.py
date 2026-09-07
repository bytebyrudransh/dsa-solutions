class Solution(object):
    def residuePrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        distinct_count = 0
        seen = set()
        residue_count = 0
        
        for i, char in enumerate(s):
            # i is 0-indexed, so length is i + 1
            length = i + 1
            
            if char not in seen:
                seen.add(char)
                distinct_count += 1
            
            if distinct_count == (length % 3):
                residue_count += 1
                
        return residue_count
        