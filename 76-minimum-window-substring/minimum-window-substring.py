class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''

        Time Complexity: O(s + t)
        - One pass scan of 't' to build the frequency array.
        - Sliding window scans and processes characters in 's' at most twice.

        Space Complexity: O(128) ≈ O(1)
        - Fixed-size arrays (ASCII) store counts for 't' and sliding window.

        To solve this problem, sliding window approach is used to determine 
        the shortest substring of 's' that contains all characters of 't' 
        with the correct multiplicities including duplicates.

        Before scanning 's', the frequency array for 't' is precomputed to
        first determine the number of characters required for the sliding 
        window to be valid. 
        
        This establishes the condition for expanding the window until it has 
        satisfied the correct number of characters required. This is achieved 
        with the use of a running counter to track the no. of characters 
        currently satisfied within the window.

        This turns the constraint into a monotonic condition:
        - Expanding the window can only increase the satisfied count.
        - Shrinking the window can only decrease it.

        With this monotonic property, the sliding window can expand until 
        all required characters from 't' are satisfied, and then shrinks from 
        the left to explore shorter substrings while still maintaining validity. 
        
        This ensures that the shortest possible substring that meets all 
        requirements is captured whenever the window is valid and updated 
        against the current best answer.
        
        '''

        freqArrT = [0] * 128 

        for char in t:
            freqArrT[ord(char)] += 1
        
        window = [0] * 128 
        required = sum(freqArrT)
        minLength = float('inf')
        start = end = current = left = 0
        
        for right, char in enumerate(s):
            if freqArrT[ord(char)]:
                if window[ord(char)] + 1 <= freqArrT[ord(char)]:
                    current += 1

                window[ord(char)] += 1

            while current == required:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    start, end = left, right

                if freqArrT[ord(s[left])]:
                    if window[ord(s[left])] <= freqArrT[ord(s[left])]:
                        current -= 1

                    window[ord(s[left])] -= 1

                left += 1

        return "" if minLength == float('inf') else s[start: end + 1]