# i will try by spamming if elif 

class Solution(object):
    def __getattr__(self,name):
        return self.solve

    def solve(self, nums):
        d = {}
         
        for i, x in enumerate(nums):
            if x not in d:
                d[x] =[1, i, 0, True]
            elif d[x][3]:
                if d[x][0] == 1:
                    d[x][2] = i - d[x][1]
                elif i - d[x][1] != d[x][2]:
                    d[x][3] = False
                    
                d[x][0] += 1
                d[x][1] = i

        return sum(1 for v in d.values() if v[0] >= 3 and v[3])            
                    









        
    
    