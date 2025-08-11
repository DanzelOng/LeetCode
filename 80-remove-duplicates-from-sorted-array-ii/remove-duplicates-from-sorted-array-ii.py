class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        To solve this problem, two pointers and a counter 'freq' 
        are used to rewrite valid numbers and track the no. of 
        times the current number has appeared. 

        Pointers 'left' tracks the position where the next valid 
        element will be copied to, whereas 'right' is used to 
        iterate through the array.

        For each number processed by 'right':

        (1) Checks if the number is different from the previous written 
        number. 
            - If so, the frequency resets to 1 to mark the start
            of the new number. 
            - Otherwise, the frequency is incremented by 1.

        (2) Checks if the current frequency is <= 2. 
            - If so, the current number at 'nums[right]' will be copied
            to 'nums[left]' and pointer 'left' moves forward.
            - Otherwise, the number is skipped, effectively removing
            excess occurrences of the current number.

        This ensures each number appears at most twice, while preserving order.
        The pointer `left` will be the length of the resulting array.

        '''
        
        freq = left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[left - 1]:
                freq = 1 
            else:
                freq += 1

            if freq <= 2:
                nums[left] = nums[right]
                left += 1
    
        return left     