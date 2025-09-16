from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        '''

        Time Complexity: O(n)
        - O(n) time scan to build the frequency map for 's'
        - O(u) time to fill buckets, where each unique character is processed once 
        - O(n) time to reconstruct resultant string

        Space Complexity: O(u)
        - u: No. of distinct characters in 's', where u <= n

        To solve this problem, we apply bucket sorting to avoid the O(nlogn) 
        overhead of sorting.

        Count the occurences for each unique character in 's' and store it
        in a frequency map. Characters are then grouped by their frequency
        in a hash table (dictionary of buckets), while tracking both the 
        maximum and minimum frequency encountered.

        To build the resultant string, iterate from the maximum frequency
        down to the minimum. For each frequency (bucket), we append each
        character in the bucket 'freq' times to the result list. At the end,
        the resultant string is returned by joining up all characters.

        '''

        maxFreq = 0
        minFreq = float('inf')
        freqMap = Counter(s)
        bucketMap = defaultdict(list)

        for char, freq in freqMap.items():
            bucketMap[freq].append(char)
            maxFreq = max(maxFreq, freq)
            minFreq = min(minFreq, freq)
        
        result = []

        for freq in range(maxFreq, minFreq - 1, -1):
            for char in bucketMap[freq]:
                result.append(char * freq)
        
        return ''.join(result)

    '''

    Standard Sorting Approach

    Time Complexity: O(nlogn) 
    Space Complexity: O(u)
    - u: no. of distinct characters in 's'

    freqMap = Counter(s)

    return ''.join(sorted(s, key=lambda char: (-freqMap[char], char)))

    '''