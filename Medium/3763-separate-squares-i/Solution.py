class Solution(object):
    def separateSquares(self, squares):
        # Calculate total area. Overlaps are counted multiple times.
        total_area = sum(float(l) * l for x, y, l in squares)
        target = total_area / 2.0
        
        # Binary search range for the y-coordinate
        low = min(y for x, y, l in squares)
        high = max(y + l for x, y, l in squares)
        
        # Precision required is 10^-5, 100 iterations provides ~10^-30 precision
        for _ in range(100):
            mid = (low + high) / 2.0
            area_below = 0.0
            
            for x, y, l in squares:
                if y >= mid:
                    continue
                elif y + l <= mid:
                    area_below += float(l) * l
                else:
                    # Square is partially below the line
                    area_below += float(l) * (mid - y)
            
            if area_below < target:
                low = mid
            else:
                high = mid
                
        return low