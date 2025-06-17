class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()

        maxCnt, i = 0, 0

        for j in range(len(s)):
            while s[j] in sett:
                sett.remove(s[i])
                i += 1
            sett.add(s[j])
            maxCnt = max(maxCnt, j - i + 1)
        
        return maxCnt