from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''

        Time Complexity: O(n)
        Space Complexity: O(n)

        To solve this problem, a sliding window of size 10 is applied
        over 's' to extract each substring, where a frequency map is 
        used to count occurences of each substring.

        A substring is a repeated sequence if it already exists in the
        frequency map. To prevent duplicates in the result, a repeated
        sequence is only added when it has a current count of 2. The 
        window than shrinks from 'left' one character at a time to find
        the substring of size 10.

        '''

        freqMap = defaultdict(int)
        result = []
        left = 0

        for right, char in enumerate(s):
            if right - left + 1 == 10:
                dna = s[left: right + 1]
                
                if freqMap[dna] + 1 == 2:
                    result.append(dna)
                
                freqMap[dna] += 1
                left += 1

        return result