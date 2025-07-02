class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        # inorder DFS returns a sorted BST
        def inorderDfs(node, arr):
            if node is None:
                return

            inorderDfs(node.left, arr)
            
            # return and skip the rest once the kth element is found
            if len(arr) == k:
                return
            else:
                arr.append(node.val)

            inorderDfs(node.right, arr)
        
        inorderDfs(root, arr)

        # the k-th smallest element will be the last in the array
        return arr[-1]