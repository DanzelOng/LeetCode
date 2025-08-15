class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        '''

        Time Complexity: O(nlogn)
        Space Complexity: O(len(arr2))

        To solve this problem, a custom comparator is used to arrange 
        the numbers of 'arr1' in such a way that all numbers appearing 
        in arr2 maintain the exact order dictated by 'arr2', whereas 
        numbers absent from 'arr2' are grouped at the end in sorted order.

        The comparator first checks whether the number exists in 'arr2' and
        inverts a result, allowing numbers present in 'arr2' to appear first.
        They are also ordered according to their position or index in 'arr2',
        which is achieved through a hash tabke lookup by mapping each number
        in 'arr2' to its index.

        For numbers absent from 'arr2', a tie-breaker is applied for them, 
        which orders them in ascending order.

        This ensures that the final ordering respects the relative order for
        numbers in 'arr2' while the remaining numbers are neatly sorted at the 
        end.
     
        '''

        def custom(num):
            return (
                num not in hashMap,
                hashMap.get(num, float('inf')),
                num
            )

        hashMap = {}

        for i in range(len(arr2)):
            hashMap[arr2[i]] = i

        arr1.sort(key=custom)

        return arr1