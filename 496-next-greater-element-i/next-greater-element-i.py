class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''

        Time Complexity: O(n + m)
        - n: scans nums2 to compute all next-greater elements
        - m: scans nums1 and returns the next greater element for every num

        Space Complexity: O(m)
        - The hash table stores m entries.
        - The stack holds a maximum of m indices in the case where nums2 
        contains a non-increasing sequence.

        To solve this problem, a monotonic stack is used to compute the next
        greater number for every number in nums2 which maintains a stack of
        indices in a non-increasing order.

        When the current number is exceeds the value of the top number in the 
        stack, this means that the current number is the "next greater element"
        for the top number, and the number is popped from the stack and records
        the mapping for the number to its current number (greater element) in 
        the hash table. 
        
        The process repeats until the stack regains its monotonically decreasing
        property, after which we push the current index. Each index is pushed 
        and popped at most once, ensuring linear time over nums2.
        
        Finally, for each value in nums1,  we return its mapped next-greater 
        value if the number exists in the hash table otherwise -1 is returned.

        '''
    
        hashMap = {}
        stack = []

        for idx, num in enumerate(nums2):
            while stack and num > nums2[stack[-1]]:
                hashMap[nums2[stack.pop()]] = num
            
            stack.append(idx)

        return [hashMap.get(num, -1) for num in nums1]