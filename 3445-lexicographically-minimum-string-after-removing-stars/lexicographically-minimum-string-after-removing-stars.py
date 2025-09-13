from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def clearStars(self, s: str) -> str:
        '''

        Time Complexity: O(n * 26) ≈ O(n)
        - For every '*' encountered, we may scan through all 26 letters 
          to find the lexicographically smallest character in O(26) time.
          Since 26 is constant, this simplifies to linear time O(n).

        Space Complexity: O(n)
        - A boolean array 'removed' of size n is used to mark deletions.
        - A hash table of lists stores indices for each character, which 
          in the worst case can hold up to n indices.

        To solve this problem, a hash table of lists is used to 
        store indices of each character encountered in the string. 
        
        When a '*' is found, it is marked for removal, and the smallest 
        lexicographical character to its left is located by checking 
        letters from 'a' to 'z' in the hash table.
        
        The rightmost occurrence of that smallest letter is then popped 
        and marked for removal.

        After processing all characters, the final string is rebuilt by
        concatenating only the characters that were not marked for removal.

        '''

        charMap = defaultdict(list)
        removed = [False] * len(s)

        for idx, char in enumerate(s):
            if char == '*':
                removed[idx] = True

                for char in ascii_lowercase:
                    if charMap[char]:
                        removed[charMap[char].pop()] = True
                        break
            else:
                charMap[char].append(idx)
        
        return ''.join([s[i] for i in range(len(s)) if not removed[i]])