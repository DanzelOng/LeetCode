class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        To solve this problem, a sliding window is applied 
        to maintain a subarray that contains at most one zero.

        A counter variable is used to track the no. of zeros
        currently present within the window. 
        
        As the window expands to the right to include new numbers, 
        it increases the count of zeros within the window if the 
        current number is zero.

        Once the no. of zeros exceed one, the window shrinks
        from 'left' until the window is valid again.
         
        The valid subarray is updated each time where the length
        is calculated as 'right' - 'left' to account for removing 
        the zero inside the window, or when the window has all ones.
        
        This process is repeated until all numbers have been 
        processed, with each number visited at most twice. 
        
        At the end, the final valid length recorded would be 
        the longest possible valid subarray after deleting 
        exactly one element.

        '''

        maxLength = zeroCount = left = 0

        for right, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
            
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                
                left += 1
            
            maxLength = max(maxLength, right - left)
        
        return maxLength