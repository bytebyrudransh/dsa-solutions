class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        
        def largestRectangleArea(heights):
            stack = [-1]
            max_a = 0
            n = len(heights)
            for i in range(n):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_a = max(max_a, h * w)
                stack.append(i)
            while stack[-1] != -1:
                h = heights[stack.pop()]
                w = n - stack[-1] - 1
                max_a = max(max_a, h * w)
            return max_a
        
        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area