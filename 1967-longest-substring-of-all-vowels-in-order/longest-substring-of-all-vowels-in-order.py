class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        A dynamic size sliding window will be used to track the 
        longest substring that contains all vowels in a non 
        decreasing and alphabetical order.

        The sliding window expands to the right as long as characters 
        appear in a non-decreasing order according to the vowel sequence.
        A counter is also used to keep track of how many distinct vowels 
        have been seen in the correct order within the current window.

        Once the counter reaches 5, the current window length is valid and
        is updated to ensure the current maximum substring length is recorded.

        If the sequence breaks, the window resets by shrinking its left 
        boundary to the current index if the character is 'a'. Otherwise,
        it goes beyond the current index to skip invalid sequences.

        '''

        maxLength = left = 0
        count = 1 if word[0] == 'a' else 0

        for right in range(1, len(word)):
            # skips characters until a valid 'a' starts a vowel sequence
            if count == 0 and word[right] != 'a':
                continue
                
            if word[right] >= word[right - 1]:
                if word[right] > word[right - 1]:
                    count += 1

                if count == 5:
                    maxLength = max(maxLength, right - left + 1) 
            
            else:
                if word[right] == 'a':
                    count = 1
                    left = right
                else:
                    count = 0
                    left = right + 1  

        return maxLength