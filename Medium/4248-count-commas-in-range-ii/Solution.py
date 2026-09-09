class Solution(object):
    def countCommas(self, n):
        total_commas = 0
        step = 1000
        
        while step <= n:
            total_commas += n - step + 1
            step *= 1000
            
        return total_commas