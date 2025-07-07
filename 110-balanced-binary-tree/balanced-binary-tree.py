class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            # base case: an empty node has no height
            if not node:
                return 0
            
            # recursively compute height of left and right subtrees
            left = height(node.left)
            right = height(node.right)
            
            # return -1 if the tree is not balanced
            # or checks if either subtree is unbalanced (has a height of -1)
            if (
                left == -1 or
                right == -1 or
                abs(left - right) > 1
            ):
                # propogate the unbalanced signal up call stack
                return -1

            # return the height of parent node (height of taller subtree of current node + 1)
            return max(left, right) + 1
        
        # a return value of -1 indicates an unbalanced tree
        return height(root) != -1