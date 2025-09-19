from collections import defaultdict
from heapq import heappush, heappop

class NumberContainers:
    '''

    Time Complexities:
    -> __init__()    : O(1)
    -> change()      : O(log n)   
    -> find()             
       Best Case     : O(1)      # top of heap is valid
       Average Case  : O(logn)   
       Worst Case    : O(nlogn)  # many stale entries in heap precedes a valid entry

    Space Complexity: O(n)

    To efficiently support index replacement and smallest-index lookups, 
    we use:
    
    (1) idxMap   : A hash table that maps each index to its current number.
    (2) numHeap  : A hash table that maps each number to a min-heap of indices 
                   that have held that number.

    Operations:

    change(): Updates the index to point to the new number and pushes the new updated
              entry into the heap. Old heap entries for this index will be discarded 
              by lazy deletion when calling find().

    find(): Repeatedly checks the top of the heap for the given number and checks it against 
            idxMap. If an entry is stale (its index no longer maps to the current number), it 
            is popped from the heap. Once a valid index is found, it is returned. If no valid 
            entries remain, return -1. 

    The lazy deletion approach avoids expensive in-heap updates when updating values. Instead, 
    stale indices are removed during find(), ensuring amortized efficiency over many operations.
    
    '''

    def __init__(self):
        self.idxMap = defaultdict(int)
        self.numHeap = defaultdict(list)
        
    def change(self, index: int, number: int) -> None:
        self.idxMap[index] = number
        heappush(self.numHeap[number], index)
        
    def find(self, number: int) -> int:
        heap = self.numHeap.get(number, [])

        while heap:
            idx = heap[0]
    
            if self.idxMap[idx] != number:
                heappop(heap)
            else:
                return idx
        
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)