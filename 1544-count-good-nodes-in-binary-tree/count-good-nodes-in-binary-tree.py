class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of no. of good nodes
        cnter = 0   

        def preorderDfs(node, maxPathSum):
            nonlocal cnter

            if node is None:
                return

            # checks if node is a good node and increment count
            # a node is good if it's node value >= current max path sum (root to current node)
            if node.val >= maxPathSum:
                cnter += 1
            
            # update maximum path sum from root to current node
            maxPathSum = max(maxPathSum, node.val)
            
            # pre-orderly traverse left and right subtrees
            preorderDfs(node.left, maxPathSum)
            preorderDfs(node.right, maxPathSum)

        preorderDfs(root, root.val)

        # return no. of good nodes
        return cnter      