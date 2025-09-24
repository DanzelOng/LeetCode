class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        Two-pointer technique is used to rearrange the array in-place. The 
        `right` pointer scans through all elements, while the `left` pointer 
        tracks the position where the next non-zero element should be placed.

        Whenever a non-zero value is found at `right`, we swap it with the value 
        at `left`. This moves all non-zero elements forward in their original 
        relative order and effectively pushes zeros toward the end of the array. 
        After swapping, `left` is incremented for the next non-zero placement.

        '''

        left = 0

        for right, num in enumerate(nums):
            if num != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums