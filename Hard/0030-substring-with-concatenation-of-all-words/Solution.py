from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        w = len(words[0])
        k = len(words)
        total = w * k
        need = Counter(words)
        n = len(s)
        result = []
        
        # Run w separate sliding windows based on offset
        for offset in range(w):
            left = offset
            count = 0                    # number of valid words currently in window
            window = defaultdict(int)
            
            # Walk in steps of w
            for right in range(offset, n - w + 1, w):
                chunk = s[right : right + w]
                
                if chunk in need:
                    window[chunk] += 1
                    count += 1
                    
                    # Shrink from left if we have too many of this chunk
                    while window[chunk] > need[chunk]:
                        left_chunk = s[left : left + w]
                        window[left_chunk] -= 1
                        count -= 1
                        left += w
                    
                    # Window holds exactly k valid words -> record and slide
                    if count == k:
                        result.append(left)
                        left_chunk = s[left : left + w]
                        window[left_chunk] -= 1
                        count -= 1
                        left += w
                else:
                    # Invalid chunk -> reset window past it
                    window.clear()
                    count = 0
                    left = right + w
        
        return result