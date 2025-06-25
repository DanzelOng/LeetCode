class Solution:
    from collections import deque, defaultdict

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # initialize queue for BFS
        queue = deque([root])

        # freq map maps each level sum to its corresponding level(s)
        # this allows us to retrieve the smallest level with the max level sum
        hashMap = defaultdict(list)

        # initialize starting level and max level sum 
        level, maxLevelSum = 1, root.val
    
        # O(n)
        while queue:
            # runningSum holds cumulative sum of node values at current level
            runningSum = 0

            # the current queue size tells us the no. of nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()
                runningSum += node.val

                # enqueue all children nodes for the next level if children exists
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            # update maximum level sum if needed
            maxLevelSum = max(maxLevelSum, runningSum)

            # record level where the sum occurs at
            hashMap[runningSum].append(level)

            # move to the next level
            level += 1

        # return the smallest level number that gives the maximum level sum
        return hashMap[maxLevelSum][0]