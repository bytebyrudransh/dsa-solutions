class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        res = []
        for x in nums:
            chars =[]
            z_threshold = 1 << 25
            #how many extra blocks in 2^25 fit into x 
            if x >= z_threshold:
                z_count = x // z_threshold
                x %= z_threshold
                chars.extend(['z'] * z_count)
            #process the remaning bits from higgest to lowest             
            bit = 24
            while bit >= 0:
                if x & (1 << bit):
                    chars.append(chr(ord('a') + bit))
                bit -= 1 
            res.append("".join(chars))
        return res
                