from collections import defaultdict
import heapq

class FoodRatings:
    '''

    Time Complexities:

    (1) __init__(): O(n)
    - n: total no. of foods in 'foods'
    - Each food is inserted to a hash table and heap, and
      heapifying all cusine heaps costs O(n) overall.
    
    (2) changeRating(): O(logm)
    - m: no. of foods for each cuisine
    - heap insertions (new ratings) into the heap costs O(logm).
    
    (3) highestRated(): average case -> O(logm), best case -> O(1)
    - Accessing the top element of a heap is O(1).
    - Outdated ratings are removed from the heap through pop operations
      that costs O(logm).
    - Otherwise, the highest rated food can be retrieved in O(1) time.

    Space Complexity: O(n)
    - The hash table stores n food entries proportional to no. of foods in 'foods'.
    - Each cuisine heap stores m food entries, and stale entries are removed overtime,
      ensuring that overall space usage for all heaps remains O(n).

    To solve this problem, we make use of 2 data structures:

    (1) A hash table maps each food to its cuisine type and current rating. This allows 
        rating lookups and updates in O(1) time and helps to check for stale entries in 
        the heap before returning the highest rated food.

    (2) A max heap is used and implemented using negation of ratings for every food.
        The heap naturally stores items in sorted order from highest rating to lowest,
        with lexicographic ordering of food names serving as a tie-breaker when two or
        more foods have the same rating.
    
    Each cuisine maintains a separate heap which stores foods starting from the highest
    rating followed by lexicographical order. On each rating change, we update the rating
    for the food in the hash table and push the new rating onto the heap. 

    To retrieve the highest rated food, we obtain the heap from the cuisine where the
    food belongs to and retrieve the top element. If the rating does not match its 
    current rating, the rating is outdated and the entry is removed from the heap. 
    Otherwise, we return the result. 

    '''

    # O(n)
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineMap = defaultdict(list)
        self.foodMap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisineMap[cuisine].append((-rating, food))
            self.foodMap[food] = [cuisine, rating]

        for cuisine, record in self.cuisineMap.items():
            heapq.heapify(record)
            
    # O(logm)
    def changeRating(self, food: str, newRating: int) -> None:
        self.foodMap[food][-1] = newRating
        cuisine = self.foodMap[food][0]
        heapq.heappush(self.cuisineMap[cuisine], (-newRating, food))

    # O(logm)
    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineMap[cuisine]
        
        while heap:
            rating, food = heap[0]  

            if self.foodMap[food][1] == -rating:
                return food

            heapq.heappop(heap)
            
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)