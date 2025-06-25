class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize hashMap to store related anagrams
        anagramMap = defaultdict(list)

        for string in strs:
            # initialize char count signature for each string
            charCount = [0] * 26

            # compute char count signature for string
            for char in string:
                charCount[ord(char) - ord('a')] += 1
            
            # group strings with the same char count signatures together
            anagramMap[tuple(charCount)].append(string)
        
        return list(anagramMap.values())