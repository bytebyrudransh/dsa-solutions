
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        prev, curr, idx = head, head.next, 1
        first = last = -1
        min_d = float('inf')
        
        while curr.next:
            if (prev.val < curr.val > curr.next.val) or (prev.val > curr.val < curr.next.val):
                if first == -1:
                    first = idx
                else:
                    min_d = min(min_d, idx - last)
                last = idx
            prev, curr, idx = curr, curr.next, idx + 1
            
        return [min_d, last - first] if first != -1 and first != last else [-1, -1]