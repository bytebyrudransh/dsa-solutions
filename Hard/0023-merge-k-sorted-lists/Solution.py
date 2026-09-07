class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def merge(l1,l2):

            dum = ListNode()
            n = dum

            while l1 and l2:
                if l1.val <= l2.val:
                    n.next = l1
                    l1 = l1.next
                else:
                    n.next = l2
                    l2 = l2.next
                n = n.next
            
            if l1: n.next = l1
            if l2: n.next = l2

            return dum.next
        
        res = None
        for l in lists:
            res = merge(res, l)
        
        return res