class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        '''

        Time Complexity: O(n * (m + k))
        - n: no. of words in 'dictionary' (bounded by 1000)
        - m: length of word 's' (bounded by 1000)
        - k: average length of words in 'dictionary' (bounded by 1000)

        Space Complexity: O(1)

        To solve this problem, we can check if each word is a subsequence
        of 's'. Two pointers are initialized for every word, with each pointer 
        traversing 's' and word, with the word pointer only advancing on 
        character matches.

        If the word pointer reaches the end, the word is a valid subsequence, 
        and it is a valid candidate for the result.
        
        The answer is updated if:
        - The word is longer than the current best word, or
        - The word has the same length but is lexicographically smaller.
        
        '''

        result = ""

        # O(n)
        for word in dictionary:
            pnterS = pnterWord = 0

            # O(m + k)
            while pnterS < len(s) and pnterWord < len(word):
                if s[pnterS] == word[pnterWord]:
                    pnterWord += 1
                pnterS += 1
            
            if pnterWord == len(word):
                if len(word) > len(result):
                    result = word
                elif len(word) == len(result):
                    result = word if word < result else result
        
        return result