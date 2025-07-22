class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        Uses a sliding window approach to find the minimum length of a 
        contiguous subarray whose sum is greater than or equal to the target.

        The window expands to include new elements by moving the right pointer,
        and contracts from the left while the window sum satisfies the condition,
        ensuring the smallest qualifying subarray is tracked throughout.

        '''

        minSize = float('inf')
        left = runningTotal = 0

        for right in range(len(nums)):
            runningTotal += nums[right]

            while runningTotal >= target:
                minSize = min(minSize, right - left + 1)
                runningTotal -= nums[left]
                left += 1

        return minSize if minSize != float('inf') else 0