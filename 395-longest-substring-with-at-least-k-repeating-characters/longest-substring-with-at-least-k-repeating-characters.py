from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ''' 

        Time Complexity: O(n * m) ≈ O(n)
        - m: no. of distinct characters in the string (bounded by 26)

        Space Complexity: O(26) ≈ O(1)
        - The window is bounded by a maximum size limit of 26 entries.

        To solve this problem, sliding window can be used to determine
        the longest substring where all characters appear >= k.

        However, 'every character appears >= k' is not a monotonic
        condition since adding one character can break the sliding 
        window.

        To make the sliding window mechanics predictable, we fix 
        a target number of distinct characters a sliding window 
        is allowed to have. 
        
        This constraint is monotonic: whereby adding a new character 
        can only increase the unique count, and shrinking the window 
        from the left can decrease it.

        As long as the sliding window is valid, we can then check
        if all characters within the window have a frequency >= k.
        If all characters >= k, the length of the current window is
        updated against the current maximum length.

        Since we do not know in advance how many different letters the 
        longest valid substring will have, the sliding window process is 
        repeated for every possible target unique count in the window
        starting from 1 to the total no. of distinct characters in 's'. 
        
        This ensures that all possible substring combinations are 
        considered and guarantees that the most optimal substring isn't 
        missed.

        '''

        distinctChars = len(set(s))
        maxLength = 0

        # O(m)
        for unique in range(1, distinctChars + 1):
            atLeastK = left = 0
            window = defaultdict(int)
            
            # O(n)
            for right in range(len(s)):
                window[s[right]] += 1
                
                if window[s[right]] == k:
                    atLeastK += 1

                while len(window) > unique:
                    if window[s[left]] == k:
                        atLeastK -= 1

                    window[s[left]] -= 1
                    
                    if window[s[left]] == 0:
                        del window[s[left]]
                    
                    left += 1

                if atLeastK == len(window):
                    maxLength = max(maxLength, right - left + 1)

        return maxLength 