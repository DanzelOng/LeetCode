from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        '''

        Time Complexity: O(nlogn)
        Space Complexity: O(1)
        - The hash table is bounded by a maximum size limit 
        proportional to the input array length (bounded by 100)

        To solve this problem, a custom comparator is used to 
        rearrange numbers with the lowest frequencies at the 
        start of the array. This is done by mapping each number 
        to its recorded frequency in a hash table and looking it up. 
        
        In the case where multiple numbers have the same frequency, 
        a tie-breaker is applied on these numbers by negating its value, 
        ensuring the larger number is placed before the smaller one.

        '''

        freqMap = Counter(nums)

        nums.sort(key=lambda num: (freqMap[num], -num))

        return nums