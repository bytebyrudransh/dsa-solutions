class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_side = 0
        
        for i in range(n):
            ax1, ay1 = bottomLeft[i]
            ax2, ay2 = topRight[i]
            
            for j in range(i + 1, n):
                bx1, by1 = bottomLeft[j]
                bx2, by2 = topRight[j]
                
                # Intersection X
                ix1 = ax1 if ax1 > bx1 else bx1
                ix2 = ax2 if ax2 < bx2 else bx2
                w = ix2 - ix1
                
                # Optimization: check width first
                if w > max_side:
                    # Intersection Y
                    iy1 = ay1 if ay1 > by1 else by1
                    iy2 = ay2 if ay2 < by2 else by2
                    h = iy2 - iy1
                    
                    if h > max_side:
                        current_side = w if w < h else h
                        max_side = current_side
                        
        return max_side * max_side