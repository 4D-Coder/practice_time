from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  # Check if the prices list is empty
            return 0

        min_price = prices[0]  # Initialize the minimum price
        max_profit = 0  # Initialize the maximum profit
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price if a lower price is encountered
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit  # Update the maximum profit if a better profit is found

        return max_profit
