class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''

        Time Complexity: O(2n) ≈ O(n)
        Space Complexity: O(n)

        To solve this problem, a monotonic decreasing stack and modulo arithmetic 
        technique are used to compute the next greater element for each number and
        handle circular array traversal, allowing each number to search circularly
        for its next greater element.

        For each number processed in nums:

        (1) The current index is mapped using modulo arithmetic (i % n) so that when 
        the iteration extends beyond n to 2n steps, the traversal wraps back to the 
        beginning of the array and simulates circular behavior.

        (2) Checks if the number is larger than the top number in the stack. If so,
        this number is the 'next greater element' and pops the top number and assigns
        it to the current number. This process is repeated until the stack restores 
        its monotonically decreasing sequence.

        (3) Only indices from the first pass (i < n) are pushed onto the stack, ensuring 
        each index is processed once.

        '''

        n = len(nums)
        stack = []
        result = [-1] * n

        for i in range(n * 2):
            idx = i % n

            while stack and nums[idx] > nums[stack[-1]]:
                result[stack.pop()] = nums[idx]

            if i < n:
                stack.append(idx)
        
        return result