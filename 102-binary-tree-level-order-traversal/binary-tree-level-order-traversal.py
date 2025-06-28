class Solution:
    from collections import deque

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # early return if tree is empty
        if not root:
            return []
        
        # initialize queue to process nodes 
        # initialize resultant array that contains subarrays of level order values
        queue, arr = deque([root]), [[root.val]]

        while queue:
            # initialize array that will contain all level order values
            levelOrderValues = []

            # current queue size indicates no. of nodes at current level
            for _ in range(len(queue)):
                # dequeue and process current node
                # perform the following steps to process it:
                # 1) enqueue all children nodes to the queue
                # 2) add the values of all children nodes to the array
                node = queue.popleft()

                if node.left:
                    levelOrderValues.append(node.left.val)
                    queue.append(node.left)
                
                if node.right:
                    levelOrderValues.append(node.right.val)
                    queue.append(node.right)
            
            # at the end of the iteration, the array will contain all values at the current level
            if levelOrderValues:
                arr.append(levelOrderValues)
        
        return arr