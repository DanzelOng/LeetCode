from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''

        Time Complexity: O(n)
        - Each index is pushed and popped from the deque at most once.
        - Both pointers move across the array in linear time.

        Space Complexity: O(k)
        - The deque can store indices of at most k elements in the
        worst case where the input contains a non-increasing sequence.

        To solve this problem, a sliding window is applied to maintain
        a valid subarray size of k while a deque maintains candidate
        indicies for the maximum number in the window.

        The deque is maintained in a monotonically decreasing sequence
        as the window expands to the right, where the front of the deque 
        stores the index of the current maximum number in the window.

        Once the window reaches size 'k', the current maximum in the
        deque is checked to see if its still within bounds of the current 
        window. If it is not, it is removed from the deque and the 'left'
        pointer moves forward to maintain the next window of size 'k'.

        This ensures that the value at the front of the deque always 
        represents the maximum value for the current window and the 
        process repeats until all numbers have been processed by 'right'. 
        
        '''
        
        deck = deque()
        result = []
        left = 0

        for right, num in enumerate(nums):
            while deck and num > nums[deck[-1]]:
                deck.pop()

            deck.append(right)
            
            if right - left + 1 == k:
                if deck[0] < left:
                    deck.popleft()
                
                result.append(nums[deck[0]])
                left += 1
        
        return result