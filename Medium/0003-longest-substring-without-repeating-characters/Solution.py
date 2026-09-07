class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hMap = {} 
        longest = ""
        current = ""
        for i, letter in enumerate(s):
            
            if letter not in hMap:
                hMap[letter] = i
            else:
                if len(current) > len(longest):
                    longest = current

                j = hMap[letter]
                current = s[j+1:i]
                hMap = {s[index]: index  for index in range(j+1,i+1)}

            current += letter
        

        return len(longest) if len(longest) > len(current) else len(current)