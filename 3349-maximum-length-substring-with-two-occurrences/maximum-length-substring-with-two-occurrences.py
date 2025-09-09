from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(n)

        To solve this problem, a sliding window is applied over 's' 
        which tracks the frequency of characters within the substring.

        As the window expands to the right, increment the frequency of
        the current character and check if it exceeds 2. If so, shrink
        the window from the left until the window is valid again. Compute
        and update the maximum substring size each time the window is valid.

        '''

        windowMap = defaultdict(int)
        maxLength = left = 0
        
        for right, char in enumerate(s):
            windowMap[s[right]] += 1
            
            while windowMap[s[right]] > 2:
                windowMap[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength