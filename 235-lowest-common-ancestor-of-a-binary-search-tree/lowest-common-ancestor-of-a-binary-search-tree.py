class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # precompute the smaller and larger values between p and q
        smallerNum, largerNum = min(p.val, q.val), max(p.val, q.val)

        def dfs(node):
            # base case: if node is between the smaller and larger values, we have found the split point
            # return this node as the LCA
            if smallerNum <= node.val <= largerNum:
                return node

            # if the current node is greater than the larger value, search on the left side of BST
            if node.val > largerNum: 
                return dfs(node.left)
            
            # search on the right side of BST
            return dfs(node.right)
        
        return dfs(root)