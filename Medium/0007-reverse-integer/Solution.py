class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Capture sign and work with absolute value
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        rev = 0
        while x:
            # Pop last digit
            digit = x % 10
            x //= 10
            
            # Push digit to result
            rev = rev * 10 + digit
            
        # Apply sign
        rev *= sign
        
        # Check for 32-bit overflow
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
            
        return rev