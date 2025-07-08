class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(node):
            if not node:
                return []

            # initialize the stack with the tuple (root, visited_flag)
            stack = [( node, False )]

            # array to store postorder traversal of values
            res = []
            
            while stack:
                nde, visited = stack.pop()

                # check if the node has children and if it is not yet visited
                if nde.children and not visited:

                    # mark the node as visited
                    stack.append(( nde, True ))

                    # add all children nodes in reversed order to the stack
                    # this allows the first child of the node to be processed
                    for i in range(len(nde.children) - 1, -1, -1):
                        stack.append(( nde.children[i], False ))

                # add the node value if it has no children or if it is already visited
                else:
                    res.append(nde.val)
            
            # return the postorder traversal array output
            return res

        return traverse(root)