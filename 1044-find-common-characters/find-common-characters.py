class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        '''

        Time Complexity: O(n * m) ≈ O(n)
        - n: no. of words in 'words' (bounded by 100)
        - m: average length of word in 'words' (bounded by 100)

        Space Complexity: O(26) ≈ O(1)
        - Two fixed-size frequency arrays of length 26 are used:
        one global array and one temporary array for each word

        To solve this problem, frequency arrays are used to store 
        character counts for each word, as well as a global frequency 
        array that tracks the minimum frequency of each character 
        seen so far. This ensures that the final result contains 
        the correct number of characters common in all words.

        For each word processed in 'words':

        - Built a temporary frequency array.

        - Checks if the word is the first word being processed. 

        - If so, update 'freqArr[i]' directly with the current 
          count in 'freqArrWord[i]'.

        - Otherwise, updating 'freqArr[i]' with the minimum count
          using 'min(freqArr[i], freqWord[i])'. This ensures that
          'freqArr' only stores counts for characters common to all
          words so far.

        After processing all words, the resultant array is reconstructed 
        by expanding each character exactly 'freqArr[i]' times.        

        '''

        freqArr = [0] * 26

        for idx, word in enumerate(words):
            freqArrWord = [0] * 26

            for char in word:
                freqArrWord[ord(char) - 97] += 1

            for i in range(26):
                freqArr[i] = min(freqArr[i], freqArrWord[i]) if idx else freqArrWord[i]

        return [chr(i + 97) for i in range(26) for _ in range(freqArr[i])]