class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
                
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
                    
        negative = (dividend < 0) ^ (divisor < 0)
               
        dvd, dvs = abs(dividend), abs(divisor)
        quotient = 0
        
        
        for i in range(31, -1, -1):
            if (dvd >> i) >= dvs:
                quotient += 1 << i
                dvd -= dvs << i
                
        return -quotient if negative else quotient