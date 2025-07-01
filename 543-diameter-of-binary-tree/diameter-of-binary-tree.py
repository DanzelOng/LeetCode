# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        
        # preorder
        def preorderDfs(node):
            nonlocal maxDiameter

            if node is None:
                return 0
            
            leftDepth = preorderDfs(node.left)
            rightDepth = preorderDfs(node.right)
            maxDiameter = max(maxDiameter, leftDepth + rightDepth)
            return max(leftDepth, rightDepth) + 1   
        
        preorderDfs(root)
        return maxDiameter

        