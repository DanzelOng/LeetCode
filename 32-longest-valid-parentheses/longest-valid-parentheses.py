class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(n)

        To solve this problem, we can use a stack to track indices of 
        unmatched '(' characters. We initialize the stack with -1 to act 
        as a starting point for calculating lengths of valid substrings.

        For every character in 's':

        (1) Checks if it is '(', and pushes its index onto the stack.

        (2) Otherwise, we pop the index of the last '(' from the stack to match
            the closing bracket.

        (3) If the stack is not empty after popping, we compute the current
            valid substring length by taking 'idx - stack[-1]' and update the 
            maximum length current seen so far.

        (4) Otherwise, the current index is pushed onto the stack to mark it as
            a new base for future valid substrings and ensure that subsequent 
            valid substrings are calculated correctly relative to this new base.
            
        At the end of the traversal, the result would contain the length of the
        longest valid parentheses substring.

        '''

        stack = [-1]
        maxLength = 0

        for idx, bracket in enumerate(s):
            if bracket == '(':
                stack.append(idx)
                continue
            
            stack.pop()

            if stack:
                maxLength = max(maxLength, idx - stack[-1])
            else:
                stack.append(idx)   
        
        return maxLength