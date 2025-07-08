class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return []

            stack = [( node, False )]
            res = []
            
            while stack:
                nde, visited = stack.pop()

                if nde.children and not visited:
                    stack.append(( nde, True ))
                    for i in range(len(nde.children) - 1, -1, -1):
                        stack.append(( nde.children[i], False ))
                else:
                    res.append(nde.val)
            
            return res

        return dfs(root)