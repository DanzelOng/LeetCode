from collections import defaultdict

class TimeMap:
    '''
    
    Time Complexities:
    - set(): O(1)
    - get(): O(logn)

    Space Complexity: O(n)

    Since timestamps given are strictly increasing, binary search 
    can be applied to efficiently search for the largest possible
    value where its timestamp <= input timestamp. Before searching, 
    each key is mapped to a list of tuple entries (value, timestamp)
    where each entry stores its value at a particular timestamp. 

    To retrieve the value of a particular key-value pair, its key
    is first checked for an entry in the hash table. If the key
    does not exists, an empty string is returned. Otherwise, the 
    corresponding list for the key is retrieved, and binary search
    is used to find the closest possible timestamp. 
    
    Two pointers - 'left' and 'right' - are initialized to mark the
    boundarys of the list and we check at each step whether the timestamp 
    at 'mid' is <= input timestamp. If so, we record its value as the 
    current best candidate where its timestamp <= input, and continue 
    searching to the right for a potentially larger timestamp. If it is 
    greater, we move the right pointer leftward to narrow the search range. 

    At the end of the binary search, if no valid timestamp exists
    (all timestamps are greater than the input), an empty string is 
    returned. Otherwise, 'result' contains the value corresponding
    timestamp <= input.

    '''

    def __init__(self):
        self.keys = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp))
  
    def get(self, key: str, timestamp: int) -> str:
        entries = self.keys[key]    
        left, right = 0, len(entries) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if entries[mid][-1] <= timestamp:
                result = entries[mid][0]    
                left = mid + 1        
            else:
                right = mid - 1
        
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)