class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # early return if tree is empty
        if not root:
            return None
        
        # initialize stack with root
        stack = [root]

        # process all nodes until stack is empty
        while stack:
            # pop and get the current node from the stack
            node = stack.pop()

            # swap left and right points
            node.left, node.right = node.right, node.left

            # add all children nodes to the stack
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            
        return root