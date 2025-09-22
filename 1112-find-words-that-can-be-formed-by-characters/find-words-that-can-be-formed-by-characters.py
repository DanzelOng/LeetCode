class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''

        Time Complexity: O(n * m) ≈ O(n)
        - n: No. of words in `words`
        - m: Average length of word `words` (bounded by 100)

        Space Complexity: O(26) ≈ O(1)

        A frequency array is used to store the count of each character in 
        `chars`. Each word in `words` is then processed using a temporary 
        frequency array to track its characters. 
        
        By comparing the word’s frequencies with those in `chars`, we can 
        determine if the word can be formed. If all characters in the word 
        appear no more times than in `chars`, the word is considered “good,” 
        and its length is added to the total sum. 

        This approach prevents repeated scans for every word and ensures the 
        solution runs in linear time relative to the total input size.

        '''

        freqArr = [0] * 26
        totalLength = 0

        for char in chars:
            freqArr[ord(char) - 97] += 1
        
        for word in words:
            freqArrWord = [0] * 26

            for char in word:
                freqArrWord[ord(char) - 97] += 1

            for i in range(26):
                if freqArrWord[i] > freqArr[i]:
                    break
            else:
                totalLength += len(word)  
 
        return totalLength