class Solution:
    def resultingString(self, s: str) -> str:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        To solve this problem, we use a stack to process characters in 's' 
        from left to right. For each character processed, we check if the 
        character at the top of the stack forms a consecutive pair with it
        (difference of 1 or wraparound 25). If so, pop the top element to
        remove the pair. Otherwise, push the current character onto the stack.

        At the end, all characters remaining in the stack represent the
        resulting string after all valid adjacent removals have been performed
        and we return the string by joining up all characters.

        '''

        stack = []
        valid = set([1, 25])

        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) in valid:
                stack.pop()
            else:
                stack.append(char)
                
        return ''.join(stack)