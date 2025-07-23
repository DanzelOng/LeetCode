class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        '''

        Time Complexity: O(n * k), where k = max length of each word
        Space Complexity: O(26) ≈ O(1)

        The idea behind this solution is to iterate through the list
        and skip any word that is an anagram of the previous word.
        To check for anagrams, we build a frequency array for each word
        and compare it to the previous word's frequency array. 

        '''

        res = []       # resultant array to store non-anagram words
        prev = None    # tracks the previous word's frequency array

        for word in words:
            # initialize frequency array for current word
            freqArr = [0] * 26
            
            # build the frequency array for current word
            for char in word:
                freqArr[ord(char) - ord('a')] += 1
            
            # add the current word to the result if it is not an anagram of the previous one
            if not prev or prev != freqArr:
                res.append(word)

                # update prev to the current word's frequency array
                prev = freqArr
        
        return res