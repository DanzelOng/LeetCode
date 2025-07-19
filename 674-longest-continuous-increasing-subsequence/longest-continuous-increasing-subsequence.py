class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        To find the longest continuous increasing subarray, 
        sliding window technique can be used.

        The sliding window is used to track the current increasing
        subarray. The window is extended as long as the current number 
        is greater than the previous number. Otherwise, the sequence is 
        invalid, and the we shrink the window from the left to mark the 
        start of a new sequence.

        '''

        left = 0        # tracks the left boundary of the sliding window
        maxLength = 1   # tracks the length of the longest increasing continuous subarray
        
        # O(n)
        for right in range(1, len(nums)):
            # extend window if numbers are part of an increasing sequence
            if nums[right] > nums[right - 1]:
                # compute and update max length if current window is longer
                maxLength = max(maxLength, right - left + 1)
            
            # sequence is invalid, shrink the window by shifting left index to right
            else:
                left = right

        return maxLength