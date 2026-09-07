class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = max_dist = 0
        n1, n2 = len(nums1), len(nums2)
        
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1
                if i > j:
                    j = i
                    
        return max_dist