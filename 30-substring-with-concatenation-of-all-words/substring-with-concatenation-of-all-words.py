from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''

        Time Complexity: O((m * k) + (n * k)) ≈ O(n)

        - m: building the freq map for 'words' requires O(m * k) time, where m <= 5000
        - k: scanning 's' requires O(n * k) time, since 's' is partitioned into tokens 
        of length k, and each token construction costs O(k). Since k <= 30, overall time
        complexity ≈ O(n)

        Space Complexity: O(u)

        - u: no. of distinct words in 'words' (bounded by 5000)

        To solve this problem, we treat 's' as a sequence of tokens of size k instead 
        of individual characters. A valid substring must therefore consist of exactly 
        len(words) tokens that match the multiset of 'words', regardless of order.

        Based on this idea, 's' can be partitioned into non-overlapping tokens of 
        length k, and a sliding window is applied over these tokens to find valid 
        substrings.

        To ensure that each token is processed only once, the search is divided into 
        k offset passes (0....k-1). For each offset, 's' is scanned in non-overlapping 
        tokens of length k, aligned to that starting offset.

        Across all offsets, about n tokens are processed, directly proportional to the 
        size of 's', preventing duplicate tokens from being processed and ensuring word 
        boundaries are respected and no valid substring is missed.

        '''

        wordMap = Counter(words)
        wordLength = len(words[0])
        required = len(words)
        indices = []

        for start in range(wordLength):
            left = start
            satisfied = 0
            windowMap = defaultdict(int)

            for right in range(left, len(s), wordLength):
                word = s[right: right + wordLength]

                if word not in wordMap:
                    satisfied = 0
                    windowMap.clear()
                    left = right + wordLength
                    continue
                
                windowMap[word] += 1
                satisfied += 1

                while windowMap[word] > wordMap[word]:
                    windowMap[s[left: left + wordLength]] -= 1
                    satisfied -= 1
                    left += wordLength
                
                if satisfied == required:
                    indices.append(left)

        return indices