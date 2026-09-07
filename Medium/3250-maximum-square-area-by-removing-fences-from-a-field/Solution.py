class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        # Add the boundary fences
        hFences = sorted(hFences + [1, m])
        vFences = sorted(vFences + [1, n])
        
        # Find all possible distances between any two horizontal fences
        h_gaps = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_gaps.add(hFences[j] - hFences[i])
        
        # Find all possible distances between any two vertical fences
        #  and check if they exist in h_gaps immediately to save space/ti me 
        max_side = -1
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                gap = vFences[j] - vFences[i]
                if gap in h_gaps:
                    max_side = max(max_side, gap)
        
        if max_side == -1:
            return -1
        
        return (max_side * max_side) % (10**9 + 7)