class Solution:
    def fib(self, n: int) -> int:
        '''

        Time Complexity: O(n)
        Space Complexity: O(1)

        To solve this problem, we use a bottom-up dynamic 
        programming approach (tabulation). Starting from 
        the base cases, we iteratively build up the sequence 
        to F(n), each time summing the two preceding numbers. 
        
        This approach avoids recursion and stack overhead, while 
        using constant space, making it both time and space efficient. 
        The result is returned after constructing the sequence up 
        to the desired index.

        '''

        if n < 2:
            return n

        dp = [0, 1]

        for _ in range(2, n + 1):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        
        return dp[1]