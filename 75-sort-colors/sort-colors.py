from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        '''

        Time Complexity: O(n + k) ≈ O(n)
        - k: The array used to store counts is fixed at size 3, 
        which is used to rewrite the original array in-place.

        Space Complexity: O(3) ≈ O(1) 
        - The size of the count array is fixed at 3.

        Since the array consists of only 3 possible values,
        a counting-sort approach can be used to efficiently 
        reconstruct the array in-place.

        A hash table is used to tally the frequencies for 
        each color in a fixed-size array of length 3.

        A pointer would then be initialized which that would 
        be used to rewrite the original array in-place with 
        the correct number of 0s, followed by 1s and 2s.

        '''

        freqMap = Counter(nums)

        counts = [0] * 3

        for num, freq in freqMap.items():
            counts[num] = freq

        pnter = 0

        for i in range(len(counts)):
            while counts[i]:
                counts[i] -= 1
                nums[pnter] = i
                pnter += 1
            
        return nums