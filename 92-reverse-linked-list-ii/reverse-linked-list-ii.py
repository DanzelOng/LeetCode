class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''

        Time Complexity: O(right) ≈ O(n), where right <= n
        Space Complexity: O(1)

        To solve this problem, pointer variables are used to reverse
        the portion of the linked list in-place between positions `left`
        and `right`. The key idea is to carefully track the nodes just 
        before and after the sublist, so that the reversed portion can 
        be seamlessly reattached.

        As such, 3 main pointers are maintained to track the following nodes:
        
        (1) prevLeft  : Node immediately before position `left`, or None 
                        if `left == 1`.

        (2) tail      : Node at position `left`, which becomes the tail 
                        of the reversed sublist.

        (3) prev      : Tracks the new head of the reversed sublist during 
                        reversal.

        (4) rightNode : Node immediately after position `right`, or None 
                        if `right` is the last node.

        Upon reversing the sublist, its tail would be connected to `rightNode` 
        whereas its head (`prev`) is reconnected back to `prevLeft` or becomes 
        the new head of the entire list if the reversal began from the first 
        node. This process ensures that the reversed segment can be joined back 
        to the original list without breaking the overall structure.

        '''

        cur = head
        prev = None

        for _ in range(left - 1):
            prev = cur
            cur = cur.next
        
        prevLeft = prev
        prev = rightNode = None
        tail = cur

        for i in range(right - left + 1):
            curNext = cur.next

            if i == right - left:
                rightNode = curNext

            cur.next = prev
            prev = cur
            cur = curNext
        
        if prevLeft is None:
            head = prev
        else:
            prevLeft.next = prev
        
        tail.next = rightNode

        return head