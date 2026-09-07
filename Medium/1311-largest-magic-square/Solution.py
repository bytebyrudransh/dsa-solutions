class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # Precompute prefix sums
        # row_pre: m rows, n+1 columns
        row_pre = [[0] * (n + 1) for _ in range(m)]
        # col_pre: m+1 rows, n+1 columns (Fixed: needs m+1 rows)
        col_pre = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                row_pre[i][j+1] = row_pre[i][j] + grid[i][j]
                
        for j in range(n):
            for i in range(m):
                col_pre[i+1][j] = col_pre[i][j] + grid[i][j]

        # Iterate size k from max possible down to 2
        for k in range(min(m, n), 1, -1):
            # Iterate through all possible top-left corners (i, j)
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    
                    # 1. Check sum of the first row
                    target = row_pre[i][j+k] - row_pre[i][j]
                    
                    match = True
                    
                    # 2. Check all rows
                    for r in range(i + 1, i + k):
                        if (row_pre[r][j+k] - row_pre[r][j]) != target:
                            match = False
                            break
                    if not match: continue
                        
                    # 3. Check all columns
                    for c in range(j, j + k):
                        if (col_pre[i+k][c] - col_pre[i][c]) != target:
                            match = False
                            break
                    if not match: continue
                        
                    # 4. Check main diagonal
                    d1 = 0
                    for d in range(k):
                        d1 += grid[i+d][j+d]
                    if d1 != target: continue
                        
                    # 5. Check anti-diagonal
                    d2 = 0
                    for d in range(k):
                        d2 += grid[i+d][j+k-1-d]
                    if d2 != target: continue
                        
                    return k
                    
        return 1