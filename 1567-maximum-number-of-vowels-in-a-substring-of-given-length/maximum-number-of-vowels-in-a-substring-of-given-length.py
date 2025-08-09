class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(5) ≈ O(1)

        To solve this problem, a fixed size sliding 
        window of size k can be used to track the 
        no. of vowels within the window.

        As the window expands to the right, a variable 
        is used to track the no. of vowels observed within 
        the current window. 
        
        Once the window reaches size k, update the maximum 
        vowel count if the current count is higher, then 
        shrink the window from the left to maintain size k.

        This process is repeated until all letters in 
        the string has been processed, ensuring the 
        maximum number of vowels in any k-length substring 
        is recorded.

        '''
        
        vowels = set('aeiou')
        maxCount = windowCount = left = 0

        for right in range(len(s)):
            if s[right] in vowels:
                windowCount += 1
            
            if right - left + 1 == k:
                maxCount = max(maxCount, windowCount)
                
                if s[left] in vowels:
                    windowCount -= 1
                
                left += 1

        return maxCount