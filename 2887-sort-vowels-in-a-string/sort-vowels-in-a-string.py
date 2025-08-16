class Solution:
    def sortVowels(self, s: str) -> str:
        '''

        Time Complexity: O(n + k) ≈ O(n)
        - k: number of distinct vowels (fixed at 10)

        Space Complexity: O(10) ≈ O(1) 
        - The hash table used to track vowel counts and the ordered 
        vowel array are both bounded by size 10, regardless of input.

        To solve this problem, a counting-based approach is applied 
        to ensure that all vowels in the string are reordered in 
        ascending ASCII order, while consonants remain fixed in their 
        original positions. 

        First, the string is scanned once to count how many times 
        each vowel appears. A fixed list of vowels in ASCII order 
        is used to provide a deterministic ordering for reconstruction.

        During the second pass, the string is rebuilt character by character:
        - If the character is a consonant, it is directly appended to the result.
        - If the character is a vowel, a pointer is used to advance through 
          the ordered vowel list until the next available vowel with a 
          non-zero count is found. That vowel is then appended, and its count
          decremented.

        This ensures that:
        1. Consonants never move from their original positions.
        2. All vowels appear in sorted ASCII order.

        '''

        vowels = set('aeiouAEIOU')

        vowelOrder = ['A','E','I','O','U','a','e','i','o','u']  

        counts = {vowel: 0 for vowel in vowelOrder}

        noVowels = True

        for char in s:
            if char in vowels:
                counts[char] += 1
                noVowels = False
       
        if noVowels:
            return s

        pnter, result = 0, []

        for char in s:
            if char not in vowels:
                result.append(char)
            else:
                # O(k)
                while pnter < len(vowelOrder) and counts[vowelOrder[pnter]] == 0:
                    pnter += 1
                
                vowel = vowelOrder[pnter]
                result.append(vowel)
                counts[vowel] -= 1
        
        return ''.join(result)