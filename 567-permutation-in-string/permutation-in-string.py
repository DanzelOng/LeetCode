class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''

        Time Complexity: O(n)
        Space Complexity: O(26) ≈ O(1)

        To solve this problem, a sliding window approach with
        frequency arrays are used to determine if 's2' contains 
        a permutation. This is done by comparing the frequency 
        arrays of 's1' and the current window of 's2'.

        The frequency array is first populated by traversing 's1',
        recording the counts for each character in the fixed-size
        array of length 26.

        The sliding window and frequency array are then initialized
        for 's2', where the window processes each character at 'right'
        and checks to see if it exists in 's1' before expanding. 
        
        If it does not exists, it means no possible permutation can 
        occur up to 'right'. Therefore, the window shrinks to 'right' 
        and the frequency array for 's2' resets for a fresh start.

        Otherwise, we update the frequency array of the current window
        and check if the size of the window is valid before checking for
        a match in both frequency arrays.

        A valid window size and frequency arrays indicates that a
        permutation exists in 's2', and returns True. If the window
        is valid but both frequency arrays do not match, the window
        shrinks from 'left' to identify possible substrings that are 
        a permutation.

        This process is repeated until all characters have been processed.

        '''

        freqArrS1 = [False] * 26

        for char in s1:
            freqArrS1[ord(char) - 97] += 1
        
        left = 0
        freqArrS2 = [0] * 26

        for right in range(len(s2)):
            if freqArrS1[ord(s2[right]) - 97] is False:
                freqArrS2 = [0] * 26
                left = right + 1
            else:
                freqArrS2[ord(s2[right]) - 97] += 1

                if right - left + 1 == len(s1):
                    if freqArrS2 == freqArrS1:
                        return True
                    
                    freqArrS2[ord(s2[left]) - 97] -= 1
                    left += 1
            
        return False