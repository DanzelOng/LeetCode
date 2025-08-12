class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(k)

        To solve this problem, a fixed-size sliding window
        of size k would be used to track valid distinct 
        subarrays together with a variable that tracks the 
        current running sum in the window.

        Before expanding the window, the current number 
        processed at 'right' is first checked if it already 
        exists in the current window before adding to the
        window. If it exists, the window is invalid, and 
        shrinks from 'left' until the duplicate is removed. 
        
        The running sum is updated throughout window 
        changes to ensure that it represents only the
        sum of all numbers in the current window.

        At the end, the window size is checked to see if it
        is size k. If so, the current running sum is compared
        against the current maximum sum and updated if it is
        larger than the maximum.

        The process is repeated until all numbers have been
        processed.

        '''

        window = set()
        maxSum = runningSum = left = 0

        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                runningSum -= nums[left]
                left += 1
            
            window.add(nums[right])
            runningSum += nums[right]

            if right - left + 1 == k:
                maxSum = max(maxSum, runningSum)
                window.remove(nums[left])
                runningSum -= nums[left]
                left += 1
        
        return maxSum