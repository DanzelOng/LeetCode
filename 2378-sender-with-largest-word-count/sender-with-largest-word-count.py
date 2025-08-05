from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        '''

        Time Complexity: O(n * k)
        - n: number of messages
        - k: maximum number of characters in a message (bounded by 100)

        Space Complexity: O(m)
        - m: number of unique senders

        To solve the problem, a hash table can be used to accumulate the 
        no. of messages for each sender. While updating the message count
        for each sender, track the sender with the current maximum word
        count. In the case of a tie, choose the lexicographically largest 
        sender.

        '''

        freqMap = defaultdict(int)
        largestSender, maxFreq = None, 0

        for sender, message in zip(senders, messages):
            freqMap[sender] += len(message.split())

            if freqMap[sender] > maxFreq:
                maxFreq = freqMap[sender]
                largestSender = sender
            
            elif freqMap[sender] == maxFreq:
                largestSender = max(largestSender, sender) if largestSender else sender

        return largestSender