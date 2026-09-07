#Tring to make it faster 
class Solution(object):
    def missingMultiple(self, nums, k):
       i=1 
       while True:
        if k*i not in nums:
            return k*i
        i+=1