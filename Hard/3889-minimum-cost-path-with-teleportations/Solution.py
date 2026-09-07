import math

class Solution:
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        # Flatten the grid to perform sorting
        # Store as (value, row, col)
        flat_cells = []
        for r in range(m):
            for c in range(n):
                flat_cells.append((grid[r][c], r, c))
        
        # Sort cells by value (ascending)
        # This allows efficient "suffix minimum" calculation
        flat_cells.sort(key=lambda x: x[0])
        
        # Map each unique value to its first appearance index in the sorted list
        # This ensures that when we teleport to a value V, we can jump from ANY cell with value >= V
        val_start_idx = {}
        for i, (val, _, _) in enumerate(flat_cells):
            if val not in val_start_idx:
                val_start_idx[val] = i

        # dp[r][c] stores the min cost to reach (r,c)
        # Initialize with infinity
        dp = [[float('inf')] * n for _ in range(m)]
        
        # Base Case: Start at (0,0) with cost 0
        dp[0][0] = 0
        
        # Initial Pass: Compute costs for 0 teleports (pure walking)
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0: continue
                
                from_top = dp[r-1][c] if r > 0 else float('inf')
                from_left = dp[r][c-1] if c > 0 else float('inf')
                
                if from_top != float('inf') or from_left != float('inf'):
                    dp[r][c] = min(from_top, from_left) + grid[r][c]

        # The answer is the min cost found so far at the bottom-right
        ans = dp[m-1][n-1]
        
        # Loop k times for k allowed teleports
        for _ in range(k):
            # 1. Prepare Teleport Costs
            # Extract costs in sorted order based on the previous iteration
            current_costs = [dp[r][c] for _, r, c in flat_cells]
            
            # Compute suffix minimums
            # suffix_min[i] = min cost among all cells from index i to end
            suffix_min = [float('inf')] * len(flat_cells)
            running_min = float('inf')
            for i in range(len(flat_cells) - 1, -1, -1):
                running_min = min(running_min, current_costs[i])
                suffix_min[i] = running_min
            
            # 2. Build Next Layer (new_dp)
            # Initialize new_dp with Teleport landings
            new_dp = [[float('inf')] * n for _ in range(m)]
            
            for i, (val, r, c) in enumerate(flat_cells):
                # We can teleport to (r,c) from any cell with value >= grid[r][c].
                # In the sorted list, this corresponds to the suffix starting at 
                # the FIRST occurrence of 'val'.
                group_start = val_start_idx[val]
                best_source_cost = suffix_min[group_start]
                
                # Teleport cost is 0, so we land with the source's cost.
                # Do NOT add grid[r][c] here because teleporting lands you "in" the cell.
                new_dp[r][c] = best_source_cost

            # 3. Propagate Normal Moves (Walking) within the new layer
            for r in range(m):
                for c in range(n):
                    curr_val = grid[r][c]
                    
                    # Try walking from top
                    if r > 0 and new_dp[r-1][c] != float('inf'):
                        new_dp[r][c] = min(new_dp[r][c], new_dp[r-1][c] + curr_val)
                    
                    # Try walking from left
                    if c > 0 and new_dp[r][c-1] != float('inf'):
                        new_dp[r][c] = min(new_dp[r][c], new_dp[r][c-1] + curr_val)
            
            # Update DP table and global answer
            dp = new_dp
            ans = min(ans, dp[m-1][n-1])
            
        return ans