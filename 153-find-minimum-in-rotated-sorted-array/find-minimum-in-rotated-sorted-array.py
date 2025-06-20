class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0 , len(nums) - 1

        while low < high:
            # compute middle number
            mid = (low + high) // 2

            # search for pivot on the right
            if nums[mid] > nums[high]:
                low = mid + 1

            # search for pivot on the left
            else:
                high = mid

        # return number at pivot index aka smallest num
        return nums[low]    