class Solution:
    def isValid(self, s: str) -> bool:
        '''

        Time Complexity: O(n)
        Space Complexity: O(n)

        To solve this problem, a stack is used keep track of opening brackets 
        as we scan each character in 's'. 
        
        When encountering a closing bracket, check if the top of the stack has 
        the matching opening bracket. If they match, pop the element at the top 
        of the stack. Otherwise, the string is invalid and we return False.

        This process is repeated until all characters have been processed and 
        the stack should be empty at the end for the string to be valid.

        '''

        stack = []
        hashMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        openingBrackets = set(['(', '[', '{'])
        
        for i in range(len(s)):
            if not stack or s[i] in openingBrackets:
                stack.append(s[i])
            elif stack[-1] != hashMap.get(s[i]):
                return False
            else:
                stack.pop()
        
        return len(stack) == 0