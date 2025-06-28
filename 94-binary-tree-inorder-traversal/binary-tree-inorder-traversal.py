# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # in-order traversal: Left - Root - Right
        stack = [root]
        res = []

        while stack:
            node = stack[-1]

            if node.left and not hasattr(node.left, 'visited'):
                stack.append(node.left)

            else:
                stack.pop()
                res.append(node.val)
                node.visited = True
                
                if node.right:
                    stack.append(node.right)
        
        return res