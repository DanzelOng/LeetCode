class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize res array,
        # where each index stores product of all nums except nums[i]
        res = [1] * len(nums)

        # intialize prefix and suffix running products
        prefixProduct = suffixProduct = 1

        for i in range(len(nums)):
            # multiple current index with product of all nums to its left,
            # and accumulate prefix running product
            res[i] *= prefixProduct
            prefixProduct *= nums[i]
            
            # mirror the same for the suffix
            res[-i - 1] *= suffixProduct
            suffixProduct *= nums[-i - 1]
        
        return res