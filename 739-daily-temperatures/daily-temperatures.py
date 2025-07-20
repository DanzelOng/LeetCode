class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''

        Time Complexity: O(n)
        Space Complexity: O(n)

        To solve this problem, a monotonically decreasing 
        stack can be used.

        A monotonically decreasing stack stores indices of 
        unresolved temperatures, ensuring constant and efficient 
        access to the most recent unresolved temperature once a 
        warmer temperature has been found.

        Once a warmer temperature is found, we can calculate the 
        difference in days taken between the cooler and warmer
        temperature by finding the difference between their indices.

        '''

        stack = []                           # stores indices of unresolved temperatures
        answer = [0] * len(temperatures)     # stores no. of days required to get a warmer temperature from the current day

        # O(n)
        for i in range(len(temperatures)):
            # while loop runs for a cumulative total of O(n) in the worst case
            # resolve and remove all previously unresolved temperatures once a warmer day is found
            while stack and temperatures[i] > temperatures[stack[-1]]:
                stackIdx = stack.pop()

                # store the number of days it took to encounter a warmer temperature
                answer[stackIdx] = i - stackIdx
            
            # add the unresolved temperature onto the stack
            stack.append(i)

        return answer