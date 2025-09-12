# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        To solve this problem, we maintain a running sum of values 
        between nodes with zeros. When the second zero is reached, 
        it marks the end of a segment. 
        
        At that point, we update the value of the first node in the 
        segment to the running sum, avoiding the need to create new nodes. 

        We then adjust the pointers to link this node into the modified 
        list, using a dummy node that points to the new head. In this way, 
        the list is rebuilt in-place by skipping the zero nodes and reusing 
        the original nodes to store the running sums.

        '''

        zerosCount = runningTotal = 0
        prev = pnter = None
        dummy = ListNode()
        cur = head

        while cur:
            runningTotal += cur.val

            if cur.val == 0:
                zerosCount += 1
            
            if cur.val and pnter is None:
                pnter = cur

            if zerosCount == 2:
                pnter.val = runningTotal
                
                if dummy.next:
                    prev.next = pnter
                else:
                    dummy.next = pnter
                
                prev = pnter
                pnter = None
                runningTotal = 0
                zerosCount = 1

            cur = cur.next
        
        prev.next = None

        return dummy.next