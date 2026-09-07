class Solution(object):
    def checkDivisibility(self, n):
        s = 0
        p = 1
        temp = n
        while temp > 0:
            digit = temp % 10
            s += digit
            p *= digit
            temp //= 10
            
        total = s + p
        return total != 0 and n % total == 0