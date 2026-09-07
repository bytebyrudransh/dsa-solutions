class Solution(object):
    def isValid(self, s):
        stack = []
        # Map closing brackets to their corresponding opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # If stack is empty or top element doesn't match, it's invalid
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        # If stack is empty, all brackets were matched correctly
        return not stack