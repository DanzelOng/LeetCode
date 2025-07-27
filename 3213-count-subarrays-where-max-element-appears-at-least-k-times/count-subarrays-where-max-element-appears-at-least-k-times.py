class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        A dynamic sliding window is used to track subarrays
        where the maximum element appears at least 'k' times.

        Two pointers - 'left' and 'right' - are used to 
        create the sliding window, where the window expands 
        until it has 'k' occurences of 'maxNum'. 
        
        At this point, subarrays that end at 'right' and 
        later will also be valid subarrays, since adding more 
        elements to the right will preserve or increase the 
        frequency of 'maxNum'. The no. of valid subarrays
        is added to the total count.

        This process is repeated while the window 
        shrinks from the left until it no longer has 
        'k' occurences of'maxNum'.

        '''
        
        maxNum = max(nums)
        cnt = freq = left = 0

        for right in range(len(nums)):
            if nums[right] == maxNum:
                freq += 1
            
            while freq == k:
                cnt += len(nums) - right

                if nums[left] == maxNum:
                    freq -= 1
                
                left += 1
        
        return cnt