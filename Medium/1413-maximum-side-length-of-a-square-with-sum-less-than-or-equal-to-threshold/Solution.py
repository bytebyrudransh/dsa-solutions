class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        
        # 1. Build 2D Prefix Sum Array
        # P[i][j] stores the sum of the rectangle from (0,0) to (i-1, j-1)
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                P[i+1][j+1] = P[i][j+1] + P[i+1][j] - P[i][j] + mat[i][j]
        
        # Helper to get sum of square with top-left (r, c) and size k
        def getSum(r, c, k):
            r2, c2 = r + k, c + k
            return P[r2][c2] - P[r][c2] - P[r2][c] + P[r][c]

        # 2. Binary Search for the maximum side length
        lo, hi = 0, min(m, n)
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            # Check if any square of size 'mid' exists with sum <= threshold
            found = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if getSum(i, j, mid) <= threshold:
                        found = True
                        break
                if found: break
            
            if found:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
                
        return ans