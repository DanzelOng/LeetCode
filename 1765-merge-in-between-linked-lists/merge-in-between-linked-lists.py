class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        '''

        Time Complexity: O(n + m)
        Space Complexity: O(1)

        Pointer variables are used to locate the nodes between
        postion `a` and after `b' in order to remove the portion 
        between these two positions (inclusive) and allow the 
        merging of `list2` to replace the deleted portion.
        
        '''

        cur = list1

        for _ in range(a - 1):
            cur = cur.next

        aPrev = cur

        for _ in range(b - a + 1):
            curNext = cur.next
            cur.next = None
            cur = curNext

        tail = cur.next
        cur = list2

        while cur and cur.next:
            cur = cur.next
        
        aPrev.next = list2
        cur.next = tail

        return list1