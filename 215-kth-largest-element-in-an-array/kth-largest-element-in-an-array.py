import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        
        Time Complexity: O(nlogk)
        Space Complexity: O(k)

        To solve this problem, a min-heap of size k is used 
        to maintain the kth largest numbers seen so far.
        
        For each number processed in the array:

        (1) If the heap contains fewer than k elements, push the number.
        (2) Otherwise, compare against the heap's minimum value:
          - If the current number is greater, pop the minimum and push 
            the current number.
          - Otherwise, the number is skipped since it cannot be among the 
            kth largest numbers.

        When all numbers in the array have been processed, the 
        heap would contain exactly k elements, with the element
        at the top being the 'kth' largest number.

        '''

        heap = []

        for num in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        
        return heapq.heappop(heap)