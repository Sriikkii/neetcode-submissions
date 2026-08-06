class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        curr_profit = 0
        selling_day = min_price+1

        for selling_day in range(len(prices)):
            if prices[selling_day] > min_price:
                curr_profit = prices[selling_day] - min_price
                max_profit = max(curr_profit,max_profit)
            if prices[selling_day] < min_price:
                min_price = prices[selling_day]
        return max_profit

        