class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        r1, c1 = source
        r2, c2 = target
        #checking color match 
        if (r1 + c1) %2 != (r2+c2)% 2:
            return -1

        #checking if they share same quibe diagonal
        if abs(r1 -r2) == abs(c1 - c2):
            return 1 

        #other they share same color 
        return 2 
        