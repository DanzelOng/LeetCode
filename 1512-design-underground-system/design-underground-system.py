from collections import defaultdict

class UndergroundSystem:
    '''

    Time Complexities:

    -> __init__()       : O(1)
    -> checkIn()        : O(1)
    -> checkOut()       : O(1)
    -> getAverageTimes(): O(1)

    Space Complexity: O(n + m)
    - n: Active customer trips being tracked.
    - m: Unique station pairs for which averages are stored.

    To efficiently track active customer trips and compute average travel times 
    between stations, we use two hash tables to store the required data.

    (1) activeTrips : Maps each customer ID to their current check-in station and 
                      time. This entry is removed when the customer checks out.
                          
    (2) commuteTimes: Maps each station-pair "start->end" to a tuple (totalTime, tripCount), 
                      accumulating travel durations and counts for average computation.

    Operations:

    checkIn(): Creates a new active trip for the customer by recording their 
               starting station and time in 'activeTrips'.

    checkOut(): Retrieves the customer's check-in details and closes the active trip.
                Computes the trip duration and updates the travel statistics for that
                station-pair by adding the new duration and incrementing the trip count.

    getAverageTime(): Retrieves the total time and trip count for the station pair 
                      from 'commuteTimes' and returns the computed average time.

    This design ensures all operations run in O(1) time using hash tables
    for direct access, with O(n) space proportional to the number of 
    active check-ins and unique station trips.

    '''

    def __init__(self):
        self.activeTrips = defaultdict(tuple)   # customerId -> (stationName, checkInTime)
        self.commuteTimes = defaultdict(tuple)  # "start->end" -> (totalTime, tripCount)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.activeTrips[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.activeTrips.pop(id)
        totalTime, tripCount = self.commuteTimes.get(f"{startStation}->{stationName}", (0, 0))
        self.commuteTimes[f"{startStation}->{stationName}"] = (t - startTime + totalTime, tripCount + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, tripCount = self.commuteTimes.get(f"{startStation}->{endStation}")
        return totalTime / tripCount

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)