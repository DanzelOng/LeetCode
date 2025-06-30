class Solution:
    from collections import deque

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # initialize a queue to process tuple of nodes from tree p and q
        queue = deque([(p, q)])

        while queue:
            # process current nodes from each tree
            nodeP, nodeQ = queue.popleft()

            # if one of the nodes are NULL, trees differ
            if (not nodeP and nodeQ) or (not nodeQ and nodeP):
                return False

            # checks the values of both nodes if both exists
            if nodeP and nodeQ:
                # value mismatch, trees differ
                if nodeP.val != nodeQ.val:
                    return False

                # enqueue left and right children for both nodes for the next comparison check
                queue.append((nodeP.left, nodeQ.left))
                queue.append((nodeP.right, nodeQ.right))
            
        return True