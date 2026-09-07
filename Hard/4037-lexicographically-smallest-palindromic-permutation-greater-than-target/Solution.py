from collections import Counter

class Solution:
    # Catch-all for any method name LeetCode expects
    def __getattr__(self, name):
        return self.solve

    def solve(self, s: str, target: str) -> str:
        counts = Counter(s)
        odds = [char for char, count in counts.items() if count % 2 != 0]
        
        if len(odds) > 1:
            return ""
            
        mid = odds[0] if odds else ""
        half_counts = {char: count // 2 for char, count in counts.items()}
        m = len(s) // 2
        
        # 1. Try exact match for the first half
        req = Counter(target[:m])
        if all(req[char] <= half_counts.get(char, 0) for char in req):
            candidate = target[:m] + mid + target[:m][::-1]
            if candidate > target:
                return candidate
                
        # 2. Backtrack to find the smallest strictly greater first half
        for i in range(m - 1, -1, -1):
            req = Counter(target[:i])
            if any(req[char] > half_counts.get(char, 0) for char in req):
                continue
                
            rem = Counter(half_counts) - req
            candidates = sorted(c for c in rem if c > target[i] and rem[c] > 0)
            
            if candidates:
                chosen = candidates[0]
                rem[chosen] -= 1
                
                half = target[:i] + chosen + "".join(
                    c * rem[c] for c in sorted(rem.keys())
                )
                return half + mid + half[::-1]
                
        return ""