class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''

        Time Complexity: O(n)
        Space Complexity: O(m), where m refers to the no.of unique numbers in the array

        # A hash table is used to track the last seen index of each unique number.
        # Once the same number is seen again, check if the difference between the
        # current and last seen index is <= k. If so, return True.
        # Otherwise, update the last seen index to the current index.

        '''

        indexMap = {}

        for i in range(len(nums)):

            if nums[i] in indexMap and i - indexMap[nums[i]] <= k:
                return True

            indexMap[nums[i]] = i

        return False