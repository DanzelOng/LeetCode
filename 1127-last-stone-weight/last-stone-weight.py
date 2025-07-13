class Solution:
    import heapq

    def lastStoneWeight(self, stones: List[int]) -> int:
        # O(n): pre-populate the max heap by first negating all stone values
        heap = [-stone for stone in stones]

        # O(n): sort the heap in place, with the heaviest stone at the top
        heapq.heapify(heap)

        # O(nlogn): repeatedly pop from the heap until it has lesser than 2 stones
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)

            # push into the heap if both stones do not have the same values
            if x != y:
                heapq.heappush(heap, y - x)
        
        # if the heap is empty, return 0, otherwise return the initial weight of last stone
        return 0 if not heap else -heap[0]