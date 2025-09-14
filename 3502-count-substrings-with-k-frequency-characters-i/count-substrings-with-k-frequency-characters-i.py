class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(26) ≈ O(1)

        To solve this problem, we apply a sliding window 
        over 's' which tracks the occurences for each 
        character in the window using a frequency array.

        As the window expands to the right, we increment the 
        frequency of the current character in the freq array 
        and check if any character has a frequency of at least k.

        If so, the current substring is valid, and substrings
        extending beyond 'right' to the end of the string will
        also be valid. The window shrinks from the 'left' as 
        we compute and update the current no. of valid substrings
        by taking 'len(s) - right' and increment 'left' forward
        until no characters appears at least k times.

        This process continues until the sliding window has process
        all characters in 's', ensuring that all valid substrings 
        are counted.

        '''

        freqArr = [0] * 26
        cnt = left = 0

        for right, char in enumerate(s):
            freqArr[ord(char) - 97] += 1

            while max(freqArr) >= k:
                cnt += len(s) - right
                freqArr[ord(s[left]) - 97] -= 1
                left += 1

        return cnt