class Solution:
    from collections import deque
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # an empty tree has no nodes to see
        if not root:
            return []

        queue = deque([root])  # initialize a queue to perform BFS
        result = [root.val]    # intialize result array that contains first visible node from the right

        while queue:
            # array to store all nodes at the current level
            lvl = []   
            
            # process all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()

                # enqueue left and right children nodes
                if node.left:
                    queue.append(node.left)
                    lvl.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    lvl.append(node.right)
            
            # add the value of the last node (rightmost) in the array 
            if lvl:
                result.append(lvl[-1].val)

        # return result array that contains all rightmost values from each level
        return result  