class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        
        Time Complexity: O(n)
        Space Complexity: O(1)
 
        This solution uses a greedy one-pass approach with a dynamic sliding window concept.

        We track two variables:
        - minPrice: the lowest price encountered so far (left boundary of the window)
        - maxProfit: the highest profit achievable based on the current price and minPrice

        For each day 'i' starting from the second item:
        (1) 
            - Check if the current price is lower than the current minimum price.
            - If so, we update minPrice to be price[i], since we have found the lower price.
            - This effectively resets the buying day to the current day.

        (2) 
            - Otherwise, we can calculate the profit at day[i] by taking prices[i] - maxProfit
            - Update maxProfit if this profit is greater than the current max profit

        By updating the lowest price each time we find a cheaper option, we ensure that 
        all profits are calculated based on the most optimal buying price seen so far.

        '''

        maxProfit = 0
        minPrice = prices[0]

        # O(n)
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - minPrice)
                
        return maxProfit