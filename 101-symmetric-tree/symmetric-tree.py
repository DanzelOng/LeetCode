class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(nde1, nde2):
            # both nodes are NULL, tree is symmetric at this level
            if not nde1 and not nde2:
                return True

            # either node is NULL, tree is not symmetrical
            if (not nde1 and nde2) or (not nde2 and nde1):
                return False
            
            # the tree is symmetrical if 
            # 1. both nodes have the same value 
            # 2. left subtree of nde1 mirrors the right subtree of nde2
            # 3. right subtree of nde1 mirrors the left subtree of nde2
            return (
                nde1.val == nde2.val 
                and isMirror(nde1.left, nde2.right) 
                and isMirror(nde1.right, nde2.left)
            )

        # O(n)
        return isMirror(root.left, root.right)