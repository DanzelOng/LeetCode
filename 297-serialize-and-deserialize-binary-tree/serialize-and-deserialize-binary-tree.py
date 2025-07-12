# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    from collections import deque
    
    def serialize(self, root) -> str:
        """
        
        This approach relies on Level Order Traversal (BFS) to serialize a tree
        to a string.

        Since BFS processes nodes level by level, it is able to effectively capture 
        the exact tree structure, including both present and missing (null) children.

        During tree traversal, each node's value is recorded in level order and from left to right. 
        If a node is missing (i.e. the child is None), the string 'null' is appended.

        At the end of the traversal, the list will be serialized into a string that accurately
        preserves the shape and completeness of the tree for deserialization.

        Time Complexity: O(n)
        Space Complexity: O(n)

        """

        if not root: return ""
        
        # initialize a queue for BFS traversal
        queue = deque([root])

        # initialize a list to store node values and NULL placeholders 
        res = []

        # O(n)
        while queue:
            # dequeue and process the node
            node = queue.popleft()

            # O(1)
            # append the node value to the list and enqueue its children to the queue
            #  for future processing if the node is not NULL
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            
            # node is NULL, append 'null' to the list
            else:
                res.append('null')

        # remove trailing NULLs until a non NULL value is reached
        while res and res[-1] == 'null':
            res.pop()
        
        # O(n): serialize the list to a string
        return ','.join(res)

    def deserialize(self, data) -> Optional[TreeNode]:
        """

        This approach relies on Level Order Traversal (BFS) to reconstruct the string 
        to the original tree structure.

        The serialized string is first parsed back to a list of tokens to prepare it 
        for level order tree reconstruction.

        A pointer and queue are used to traverse the parsed list and rebuild the tree in 
        level order:
            
            - The pointer keeps track of the current position in the list.
            - For each node dequeued to be processed, we assign its left and right children.
              based on the next 2 tokens in the list through the pointer if it is within bounds
            - The pointer is incremented each time a child is assigned.
            - If the pointer is out of bounds, we know the node has no children.
        
        At the end of the traversal, the tree will be successfully reconstructed into its original 
        structure.

        Time Complexity: O(n)
        Space Complexity: O(n)

        """
        
        # return if there is no serialized data
        if not data: return

        # O(n): parses the serialized string into a list of tokens
        # to prepare level order tree reconstruction
        nodes = data.split(',')

        # set the root node to the first node in the list
        root = TreeNode(val=int(nodes[0])) 

        # initialize a queue for BFS traversal
        queue = deque([root])                 

        # intialize a pointer for traversing the list                                  
        pnter = 1         

        # tracks the size of the list to perform index bounds checking            
        n = len(nodes)                       

        # O(n)
        while queue:
            node = queue.popleft()

            # O(1): dynamically assigns left and right child of current node
            for child in ('left', 'right'):

                # if pointer is out of bounds, we know the node has no children; exit the loop
                if pnter >= n:
                    break
                
                # set child as None if pointer points to NULL
                if nodes[pnter] == 'null':
                    setattr(node, child, None)

                # index points to a new node, create and set child as new node
                else:
                    newNode = TreeNode(val=int(nodes[pnter]))
                    setattr(node, child, newNode)

                    # enqueue the new node to be processed in the future
                    queue.append(newNode)

                # advance pointer forward in the serialized list
                pnter += 1 
        
        return root

        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))