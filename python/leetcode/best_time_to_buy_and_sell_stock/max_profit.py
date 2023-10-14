from typing import List
import ipdb

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    profit_tracker = []
    for i in prices:
      sell_prices = prices.index(i) + 1
      if len(prices) == 1:
        return 0
      else:
        for e in prices[sell_prices:]:
          profit = e - i
          profit_tracker.append(profit)

    max_profit = max(profit_tracker)
    return 0 if max_profit <= 0 else max_profit
