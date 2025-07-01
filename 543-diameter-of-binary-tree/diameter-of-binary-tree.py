class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # keeps track of the maximum diameter
        maxDiameter = 0

        # helper function used to post-orderly traverse the tree
        def postorderDfs(node):
            nonlocal maxDiameter

            # an empty tree (NULL) has no edge
            if node is None:
                return 0
            
            # recursively compute no. of edges for left and right subtrees of current node
            leftEdges = postorderDfs(node.left)
            rightEdges = postorderDfs(node.right)
            
            # compute current diameter and update maximum diameter if needed
            # diameter = left subtree depth + right subtree depth (in edges)
            maxDiameter = max(maxDiameter, leftEdges + rightEdges)

            # return the greater depth (in edges) of the 2 subtrees of the current node
            # +1 accounts for the additional edge from the current node to its parent
            return max(leftEdges, rightEdges) + 1   
        
        postorderDfs(root)
        return maxDiameter       