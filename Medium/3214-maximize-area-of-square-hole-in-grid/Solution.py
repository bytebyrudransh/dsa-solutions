class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        # Helper function to find the maximum consecutive gap
        def get_max_gap(bars):
            bars.sort()
            max_len = 1
            current_len = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_len += 1
                else:
                    current_len = 1
                max_len = max(max_len, current_len)
            
            # If we remove 'k' consecutive bars, the hole size becomes k + 1
            return max_len + 1

        # Calculate max gap for horizontal and vertical bars
        h_gap = get_max_gap(hBars)
        v_gap = get_max_gap(vBars)
        
        # The largest square side is limited by the smaller of the two gaps
        side = min(h_gap, v_gap)
        
        return side * side