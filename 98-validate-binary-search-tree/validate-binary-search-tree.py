class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorderDfs(node, arr):
            if node is None:
                return
            
            inorderDfs(node.left, arr)
            arr.append(node.val)
            inorderDfs(node.right, arr)
        
        inorderDfs(root, arr)

        # check if the inorder traversal yields a strictly increasing sequence
        for i in range(len(arr) - 1):
            if arr[i + 1] <= arr[i]:
                return False
            
        return True