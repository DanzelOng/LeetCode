class Solution:
    from collections import deque
    import heapq

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = [root.val]      # initialize a min heap to keep track of kth largest sum
        queue = deque([root])  # initialize a queue for BFS traversal

        # O(n)
        while queue:
            runningTotal = 0

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    runningTotal += node.left.val
                    queue.append(node.left)
                
                if node.right:
                    runningTotal += node.right.val
                    queue.append(node.right)

            # O(logk): min heap of size k ensures the kth largest sum of current window to be the root node
            if runningTotal:
                if len(heap) < k:
                    heapq.heappush(heap, runningTotal)
                else:
                    heapq.heappushpop(heap, runningTotal)
        
        # return immediately if there are fewer than k levels
        if len(heap) < k:
            return -1
        
        # Total Time Complexity of Algorithm: O(nlogk)
        return heapq.heappop(heap)