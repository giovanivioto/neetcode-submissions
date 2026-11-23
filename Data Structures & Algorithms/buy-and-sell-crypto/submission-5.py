class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##o(n) time
        ##o(1) space

        maximum = 0
        minimum = 0
        profit = 0
        for i, price in enumerate(prices):
            if i != 0:
                if price < prices[minimum]:
                    minimum = i
                    maximum = i
                elif price > prices[maximum]:
                    maximum = i

                profit = prices[maximum] - prices[minimum] if (prices[maximum] - prices[minimum]) > profit else profit

        return profit