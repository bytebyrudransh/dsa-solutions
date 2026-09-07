class Solution(object):
    def countPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        
        counts = defaultdict(int)
        pairs = 0
        
        for word in words:

            base = ord(word[0])
            key = tuple((ord(char) - base) % 26 for char in word)
            

            pairs += counts[key]
            counts[key] += 1
            
        return pairs