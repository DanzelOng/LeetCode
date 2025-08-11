class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        To solve this problem, two pointers will be used 
        to rewrite valid numbers and remove duplicates.

        Pointers 'left' mark the position where the valid
        number would be copied to, whereas 'right' is used
        to traverse through the array.

        For each number processed by 'right', we check if 
        it is same as the previously written number. 
        
        If so, we know that the number is a duplicate, 
        and skip over it, ensuring that no duplicates 
        would be found in the valid portion of the array. 
        
        Otherwise, the number is a new unique number, and 
        we copy the number to the position at 'left' and 
        move 'left' forward.
        
        At the end, pointer 'left' will be the length of the
        resulting array with no duplicates.

        '''

        left = 1

        for right in range(1, len(nums)):
            if nums[right] == nums[left - 1]:
                continue
            
            nums[left] = nums[right]
            left += 1
        
        return left