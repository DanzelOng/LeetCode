class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''

        Time Complexity: O(2n) ≈ O(n)
        Space Complexity: O(n)

        The list is reversed using recursion. We traverse recursively 
        until the last node, which becomes the new head of the list. 
        
        As the recursion unwinds, each node’s `next` pointer is 
        redirected to point back to itself, and its `next` pointer 
        is set to None to break the forward link.

        This process ensures that all links are reversed step by step, 
        as the new head is returned up the call stack.

        '''

        def recurse(node):
            if node.next is None:
                return node
            
            head = recurse(node.next)
            node.next.next = node
            node.next = None

            return head
        
        return recurse(head) if head else None
    
    '''

    Two Pointer Approach

    Time Complexity: O(n)
    Space Complexity: O(1)
    
    cur = head
    prev = None

    while cur:
        curNext = cur.next
        cur.next = prev
        prev = cur
        cur = curNext
    
    return prev

    '''