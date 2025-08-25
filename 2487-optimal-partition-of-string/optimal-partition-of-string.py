class Solution:
    def partitionString(self, s: str) -> int:
        '''

        Time Complexity: O(n)
        - Each character is processed once in a single pass.
        - Resetting the frequency array is O(26), which is constant.

        Space Complexity: O(26) ≈ O(1)
        - Fixed-size array of length 26 is used regardless of input size.

        To solve this problem, we greedily build substrings from left to right 
        while ensuring that each substring contains only unique characters. To 
        do so, a frequency array is used to track characters that have appeared 
        in the current substring.

        For each character processed:

        (1) Checks if the character exists in the frequency array.

        (2) If it exists, the character is a repeating character. The count of 
        substrings is incremented and the frequency array resets to include the 
        character as the start of the new substring.

        (3) Otherwise, the character is recorded in the frequency array and added
        to the current substring.

        This approach ensures that a split occurs at the first repeated character,
        and ensures the minimum no. of substrings while never backtracking.

        '''

        freqArr = [0] * 26
        counts = 1

        for char in s:
            if freqArr[ord(char) - 97]:
                counts += 1
                freqArr = [0] * 26
            
            freqArr[ord(char) - 97] = 1

        return counts