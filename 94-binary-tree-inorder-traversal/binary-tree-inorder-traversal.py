class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # in-order traversal: Left -> Root -> Right
        stack = [root]
        visited = set()
        res = []

        while stack:
            node = stack[-1]

            if node.left and node.left not in visited:
                stack.append(node.left)

            else:
                stack.pop()
                res.append(node.val)
                visited.add(node)
                
                if node.right:
                    stack.append(node.right)
        
        return res