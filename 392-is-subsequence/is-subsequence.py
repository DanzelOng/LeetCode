class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''

        Time Complexity: O(n)
        - In the average/worst case, we need to scan the entire string 't' to find a valid subsequence

        Space Complexity: O(1)
        - Two pointers are used regardless of input size

        To solve this problem, two pointers are used to traverse both 
        strings concurrently. At each index, we check if the characters 
        from both strings match each other. If so, we increment the 
        pointer for 's' and 't' forward. Otherwise, only the pointer for 
        't' is incremented.

        This process is repeated until either pointers have reached the 
        end of their respective strings. At the end, check if the pointer 
        for 's' has reached the end of the string. If so, all characters 
        in 's' has been found in 't' (i.e 's' is a subsequence) and we return 
        True. Otherwise, return False.

        '''

        sPnter = tPnter = 0

        while sPnter < len(s) and tPnter < len(t):
            if s[sPnter] == t[tPnter]:
                sPnter += 1
            tPnter += 1

        return sPnter == len(s)