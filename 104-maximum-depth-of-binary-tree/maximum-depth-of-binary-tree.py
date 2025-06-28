class Solution:
    from collections import deque

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # an empty tree has a depth of 0
        if not root:
            return 0

        queue = deque([root])   # initialize queue for level-order-traversal
        level = 0               # tracks current depth of tree 

        while queue:
            # process all nodes at current level
            for _ in range(len(queue)):
                node = queue.popleft()

                # enqueue all child nodes for the next level
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            # increment depth counter after processing current level
            level += 1
        
        # return final depth after traversing all levels
        return level