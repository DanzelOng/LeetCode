class Solution:
    def customSortString(self, order: str, s: str) -> str:
        '''

        Time Complexity: O(n)
        Space Complexity: O(26) ≈ O(1)

        A frequency array is first used to record 
        the no. of times each character appears in 
        's'. This is needed for reconstructing the
        resultant string with the correct frequencies 
        for each character.

        To ensure that all characters in 'order' appear
        first, we iterate through 'order' and append to
        an array based on the no. of times it appears by
        looking up the frequency array. 
        
        Before moving on to the next character, mark the
        frequency of the current character as 0 to mark 
        it as processed.

        After finishing `order`, iterate through the frequency 
        array. Characters with a remaining count represents 
        those that were not present in 'order', and are appended 
        to the array in alphabetical order.

        At the end, the array would first contain characters
        present in 'order' with the correct order and frequency,
        with remaining characters in sorted order.

        The resultant string is returned by joining all characters 
        in the array.

        '''

        freqArrS = [0] * 26

        for char in s:
            freqArrS[ord(char) - 97] += 1
        
        result = []

        for char in order:
            result.append(char * freqArrS[ord(char) - 97])
            freqArrS[ord(char) - 97] = 0
                    
        for i in range(26):
            if freqArrS[i] > 0:
                result.append(chr(i + 97) * freqArrS[i])
        
        return ''.join(result)