class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        '''

        Time Complexity: O((m + n) * k) ≈ O(n)
        - m: number of words in 'words2'
        - n: number of words in 'words1'
        - k: maximum word length (≤ 10)

        Space Complexity: O(26) ≈ O(1)
        - 2 fixed size frequency arrays are used (requirement array and 
        temporary array per word in 'words1')
        - Does not include output list in complexity

        To solve this problem, a global requirement frequency array is
        computed from 'words2' that records the maximum frequency needed
        for each character across words in 'words2'. This ensures that
        the array captures the strictest requirement for every character
        across 'words2'.

        Next, for each word processed in 'words1':

        (1) Built its frequency array.

        (2) Compare the word's freq array against the requirement array. 
            If at any point, the frequency in the requirement array exceeds 
            the word's available frequency, the word is not universal and 
            the check is stopped.
        
        (3) If the word satisfies all character requirements by the end of
            the comparison, it is universal and added to the result.

        This ensures that the resultant array contains all universal strings.

        '''

        freqArr = [0] * 26

        # O(m)
        for word in words2:
            freqArrWord = [0] * 26

            # O(k)
            for char in word:
                freqArrWord[ord(char) - 97] += 1
            
            for i in range(26):
                freqArr[i] = max(freqArr[i], freqArrWord[i])
        
        universalStrings = []

        # O(n)
        for word in words1:
            freqArrWord = [0] * 26

            # O(k)
            for char in word:
                freqArrWord[ord(char) - 97] += 1
            
            for i in range(26):
                if freqArr[i] > freqArrWord[i]:
                    break
            else:
                universalStrings.append(word)
        
        return universalStrings