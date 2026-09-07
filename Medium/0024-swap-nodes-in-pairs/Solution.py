class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
            
        first, second = head, head.next
        
        # Recursively swap the rest of the list
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second