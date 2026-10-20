class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        msf = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            msf = max(msf, price - lowest)
        return msf