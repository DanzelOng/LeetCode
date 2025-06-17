class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pivot-free based approach
        # approach relies on finding the sorted half as anchor of truth
        # once sorted half is identified, perform following steps:
        # 1) check if target is found within the sorted half 
        # 2) narrow search within sorted half if target is within this half
        # 3) otherwise, shift search to other half
        # 4) repeat process until search space is exhausted 

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # left side is sorted half
            elif nums[low] <= nums[mid]:
                # target is within this sorted half, search within this half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                
                # target not within this sorted half, search the other half
                else:
                    low = mid + 1

            # left side is sorted half
            else:
                # target is within this sorted half, search within this half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1

                # target not within this sorted half, search the other half
                else:
                    high = mid - 1

        return -1 