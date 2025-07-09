class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, val):
            # return 0 when node is NULL since no good nodes were encountered
            if node is None:
                return 0
            
            # update max value seen so far from root to current node
            val = max(val, node.val)

            # checks if current node is a good node and perform boolean to integer casting to count no. of good nodes
            # perform the same check on the left and right subtree of current node
            return int(node.val >= val) + dfs(node.left, val) + dfs(node.right, val)
        
        return dfs(root, root.val)