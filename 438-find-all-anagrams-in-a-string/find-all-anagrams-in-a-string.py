class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''

        Time Complexity: O(n)
        Space Complexity: O(26) ≈ O(1)
        - Fixed-size frequency arrays of length 26 are used regardless of input size.

        '''

        anagramCount = [False] * 26  # initialize frequency array for the anagram 'p'
        charCount = [0] * 26         # initialize frequency array to track frequencies for current window of 's'        

        # build the frequency array for anagram 'p'
        for i in range(len(p)):
            anagramCount[ord(p[i]) - ord('a')] += 1
        
        l = 0      # initialize left pointer (left boundary of window)
        res = []   # initialize array to store start indices of all anagrams

        # O(n)
        for r in range(len(s)):
            # reset the window if current character not in 'p'
            if anagramCount[ord(s[r]) - ord('a')] is False:
                l = r + 1                      # move left pointer to the next index
                charCount = [0] * 26           # clear current window frequencies
                continue
            
            # build frequency array for current window of 's'
            charCount[ord(s[r]) - ord('a')] += 1

            # while loop runs for a cumulative total of O(n)
            # check for an anagram match once window size equals length of 'p'
            while r - l + 1 == len(p):
                # found a valid anagram starting at index 'l'
                if charCount == anagramCount:
                    res.append(l)

                # shrink window from the left and increment left pointer
                charCount[ord(s[l]) - ord('a')] -= 1
                l += 1
        
        return res   