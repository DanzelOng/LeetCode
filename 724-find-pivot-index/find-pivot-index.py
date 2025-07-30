class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        
        Time Complexity: O(n)
        Space Complexity: O(1)
  
        To solve this problem, we check every index as a potential pivot
        where the sum of elements on the left equals the sum on the right.

        To avoid recalculating left and right sums repeatedly, we:
        
        (1) Compute the total sum of the array first.
            This represents the combined weight of all elements.

        (2) Traverse the array from left to right while maintaining a running
            sum of all elements to the left of the current index.

            At each index 'i':
            - Left sum is simply the running sum.
            - Right sum can be derived by subtracting the current element and 
              running sum from total:
                rightSum = total - nums[i] - runningSum

            If left sum == right sum, then index 'i' is a valid pivot index.

        (3) If no such index is found after traversing the array, return -1.

        '''

        total = sum(nums)
        runningSum = 0

        for i in range(len(nums)):
            if runningSum == total - runningSum - nums[i]:
                return i
            runningSum += nums[i]

        return -1       