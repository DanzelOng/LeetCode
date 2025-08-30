class Solution:
    def longestWord(self, words: List[str]) -> str:
        '''

        Time Complexity: O(nlogn + n * m) ≈ O(nlogn)
        - Sorting takes O(nlogn).
        - For each word, checking its prefix `word[:-1]` requires O(m) slicing,
        making the iteration phase O(n·m).
        - Since m <= 30, this reduces to O(n).

        Space Complexity: O(n)
        - A hash set is used to store n words in 'words'.

        To solve this problem, words are first sorted by non-decreasing length 
        so that shorter words are always processed before longer ones. This 
        ensures that when checking a word, its prefix will already be in the 
        set if it is buildable. 

        For each word processed:

        (1) If its length is 1, or if its prefix 'word[:-1]' exists in the set, 
        it is marked as buildable and added to the set.

        (2) If the word exists in the set, it is a valid candidate for the result.
        The answer is updated if:
        - The word is longer than the current best word, or
        - The word has the same length but is lexicographically smaller.

        This guarantees that the final answer is the longest word that can be 
        built step by step from other words in the dictionary, with ties 
        resolved lexicographically.

        '''

        words.sort(key=len)
        sett = set()
        maxLength = 0
        indice = -1

        for idx, word in enumerate(words):
            if len(word) == 1 or word[:-1] in sett:
                sett.add(word)
            if word in sett:
                if len(word) > maxLength: 
                    maxLength = len(word)
                    indice = idx
                elif len(word) == maxLength:
                    indice = idx if word < words[indice] else indice
        
        return words[indice] if indice >= 0 else ""