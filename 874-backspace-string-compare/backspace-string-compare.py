class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''

        Time Complexity: O(s + t)
        Space Complexity: O(1)

        To solve this problem, two pointers and skip counter variables 
        for strings 's' and 't' are used to keep track of the current 
        characters and no. of backspaces encountered. 

        By keeping track of the no. of backspaces encountered for each 
        string, this indicates the no. of times we can skip over a 
        non-backspace character. A while loop is used to traverse both
        strings concurrently until a valid character is reached
        (i.e: a non-backspace character and no. of backspaces encountered = 0).

        Compare the current characters from both strings, both strings are 
        not equal if:
        (1) Their pointers are within bounds and characters do not match
        (2) One string has been fully processed but the other still has characters left

        This process is repeated until both strings have been processed 
        with no mismatches, which indicates that both strings are equal.

        '''

        skipCountS = skipCountT = 0
        pnterS, pnterT = len(s) - 1, len(t) - 1

        while pnterS >= 0 or pnterT >= 0:

            while pnterS >= 0:
                if s[pnterS] == '#':
                    skipCountS += 1
                elif skipCountS != 0:
                    skipCountS -= 1
                else:
                    break
     
                pnterS -= 1
 
            while pnterT >= 0:
                if t[pnterT] == '#':
                    skipCountT += 1
                elif skipCountT != 0:
                    skipCountT -= 1
                else:
                    break

                pnterT -= 1
            
            # strings cannot be equal when one string has been fully processed and the other has not
            if (pnterS >= 0) != (pnterT >= 0):
                return False

            # both valid characters do not match
            if pnterS >= 0 and pnterT >= 0 and s[pnterS] != t[pnterT]:
                return False
            
            pnterS -= 1
            pnterT -= 1
        
        return True