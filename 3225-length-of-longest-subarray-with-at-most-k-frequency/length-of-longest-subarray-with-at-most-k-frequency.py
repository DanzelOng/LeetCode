from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(n)

        A dynamic sliding window is used to track subarrays
        with numbers that have at most 'k' frequency.

        To track the frequency of each number within the
        window, a hash table is used.

        Two pointers - 'left' and 'right' - are used to
        create the sliding window, where the window expands
        to the rightuntil inserting a number causes its 
        frequency to exceed 'k'. 
        
        The window then shrinks from the left until the 
        frequency constraint is maintained. At each step,
        the maximum length of the valid window is updated.

        '''

        windowMap = defaultdict(int)
        maxLength = left = 0

        for right in range(len(nums)):
            windowMap[nums[right]] += 1

            while windowMap[nums[right]] > k:
                windowMap[nums[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)
            
        return maxLength