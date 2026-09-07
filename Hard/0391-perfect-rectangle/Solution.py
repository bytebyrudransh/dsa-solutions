class Solution(object):
    def isRectangleCover(self, rectangles):
        area = 0
        corners = set()
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')

        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            
            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
        
        if len(corners) != 4:
            return False
            
        return area == (max_x - min_x) * (max_y - min_y) and \
               all(p in corners for p in [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)])