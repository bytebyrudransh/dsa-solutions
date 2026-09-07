class Solution:
    def countRotations(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for i in range (n):
            rot = s[i:] + s[:i]
            score = sum(rot [j] == rot[j+1] for j in range (n-1))
            if score == k:
                ans +=1
        return ans        
        