class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        To find the longest subarray containing at most `k` zeros,
        a dynamic sliding window approach is used.

        The window expands to the right as long as the number of zeros
        does not exceed `k`. If it does, the window shrinks from the
        left until it becomes valid again.

        A variable is maintained to track the maximum valid window length
        throughout the iteration.

        '''

        maxLength = numZeros = left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                numZeros += 1
            
            while numZeros > k:
                if nums[left] == 0:
                    numZeros -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)     
        
        return maxLength