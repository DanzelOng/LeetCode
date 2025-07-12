class Solution:
    from collections import Counter
    from heapq import heapify, heappop
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # O(n): tabulate frequencies of each word
        freqMap = Counter(words)

        # O(n): pre-populate the max heap with tuples 
        # containing the negated word frequency and word
        heap = [(-freqMap[word], word) for word in freqMap]

        # O(n): sorts the heap in place by arranging tuples starting
        # with the highest frequency, followed by lexicographical order
        heapify(heap)
        
        # Total Time Complexity: O(n + klogn)
        return [heappop(heap)[-1] for _ in range(k)]