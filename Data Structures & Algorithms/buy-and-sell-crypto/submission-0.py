class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        start on i, create a window from i + 1 - len(lst)
        - find the max in the list and subtract from your current i
        - store this into a variable that will find the max you can make
        '''
        max_profit = float('-inf')
        for i in range(len(prices)):
            window = prices[i + 1: len(prices)]
            if window:
                biggest_profit = max(window)
            else:
                biggest_profit = 0
            
            max_profit = max(max_profit, biggest_profit - prices[i])

        if max_profit < 0:
            return 0
        else:
             return max_profit

