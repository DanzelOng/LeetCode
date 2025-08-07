class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        To solve this problem, we can make use of ascii values with
        a sliding window to determine if the current character is 
        exactly one value greater than the previous character. If yes, 
        we expand the window and update the maximum length seen so far.

        At the end of the iteration, the maximum window length recorded 
        will represent the length of the longest alphabetical continuous 
        substring.

        '''

        left, maxLength = 0, 1

        for right in range(1, len(s)):
            if s[right] == chr(ord(s[right - 1]) + 1):
                maxLength = max(maxLength, right - left + 1)
            else:
                left = right
        
        return maxLength