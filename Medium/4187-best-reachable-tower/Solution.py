class Solution(object):
    def bestTower(self, towers, center, radius):
        cx, cy = center
        best = [-1, -1]
        best_q = -1

        for x, y, q in towers:
            if abs(x - cx) + abs(y - cy) <= radius:
                if q > best_q or (q == best_q and (best == [-1, -1] or [x, y] < best)):
                    best_q = q
                    best = [x, y]

        return best