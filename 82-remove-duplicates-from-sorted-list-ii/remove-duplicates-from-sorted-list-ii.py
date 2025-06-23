# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            # checks if current node starts a duplicate sequence
            if cur.next and cur.val == cur.next.val:
                val, cur = cur.val, cur.next

                # skips all duplicate nodes
                while cur and cur.val == val:
                    cur = cur.next

                # edge case handling: if duplicate sequence is at the head
                if head.val == val:
                    # update head to be the next unique node
                    head = prev = cur
                
                # update the prev node to point to the next unique node
                else:
                    prev.next = cur
            
            # no duplicates, move prev and cur pointers forward
            else:
                prev = cur
                cur = cur.next
        
        return head