class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        '''

        Time Complexity: O(n)
        Space Complexity: O(n)

        '''

        def dfs(node, char):
            if node is None:
                return
            
            # build the string from the bottom up by prepending current character
            char = chr(ord('a') + node.val) + char

            if node.left and node.right:
                # compares and returns the lexicographically smallest string from both sides
                return min(
                    dfs(node.left, char),
                    dfs(node.right, char)
                )
            
            # recurse on the left if node only has a left child
            if node.left:
                return dfs(node.left, char)
            
            # recurse on the right if node only has a right child
            if node.right:
                return dfs(node.right, char)
            
            # node is a leaf node, return the constructed string 
            return char
        
        return dfs(root, '')