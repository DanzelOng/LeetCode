class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        '''

        Time Complexity: O(nlogn)
        Space Complexity: O(n)

        To solve this problem, each number in 'nums' is transformed into 
        its mapped value by rebuilding it digit by digit according to 
        the mapping rules. The mapped value is formed arithmetically, so 
        any leading zeros produced during the transformation naturally 
        drop off when converted to an integer.

        For each number in 'nums':

        - Construct its mapped value digit by digit.
        - Store the result as a tuple containing the mapped value, its index, 
        and the original number.

        Each tuple stores:

        (1) The mapped value (used as the sorting key).
        (2) The original index (to preserve relative order for ties).
        (3) The original number (for producing the final output).

        After building all tuples, the list is sorted in ascending order 
        by the mapped values. The resultant array is then produced by 
        extracting the original numbers from the tuples.

        '''

        arr = []

        for idx in range(len(nums)):
            num = str(nums[idx])
            mappedVal = mapping[int(num[0])]
            
            for i in range(1, len(num)):
                mappedVal = mappedVal * 10 + mapping[int(num[i])] 
            
            arr.append((mappedVal, idx, nums[idx]))

        arr.sort()
        
        return [tup[-1] for tup in arr]