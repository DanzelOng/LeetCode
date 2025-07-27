class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(3) ≈ O(1)

        To solve this problem, we can use sliding window to keep track 
        of valid substrings that contain all 3 characters.

        To keep track the counts of each character in the current window, 
        a fixed-size frequency array of length 3 is used.

        (1) The window expands to the right until all three characters 
        are present. For each valid window ending at 'right', all 
        substrings starting from the current 'left' up to right (and beyond)
        will also be valid and guaranteed to contain all three characters.

        (2) We count all valid substrings at this point by adding (len(s) - right)
        to the current count, before shrinking the window from the left to 
        find smaller valid substrings until 1 of 3 characters are no longer
        present in the current window.

        Steps (1) to (2) are repeated until all characters in the string 
        has been processed.

        '''

        freqArr = [0] * 3
        cnt = left = 0

        for right in range(len(s)):
            freqArr[ord(s[right]) - ord('a')] += 1

            while all(freqArr):
                cnt += len(s) - right
                freqArr[ord(s[left]) - ord('a')] -= 1
                left += 1
        
        return cnt