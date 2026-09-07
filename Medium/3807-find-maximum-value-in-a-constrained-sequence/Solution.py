class Solution(object):
    def findMaxVal(self, n, restrictions, diff):
        limits = [float('inf')] * n
        limits[0] = 0

        for idx, val in restrictions:
            limits[idx] = min(limits[idx], val)

        for i in range(1, n):
            limits[i] = min(limits[i], limits[i - 1] + diff[i - 1])

        for i in range(n - 2, -1, -1):
            limits[i] = min(limits[i], limits[i + 1] + diff[i])

        return max(limits)