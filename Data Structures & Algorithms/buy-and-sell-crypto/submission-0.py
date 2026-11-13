class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_cost = prices[0]
        max_pro = 0

        for i in range(len(prices) - 1):
            if low_cost > prices[i + 1]:
                low_cost = prices[i + 1]
            else:
                if max_pro < (prices[i + 1] - low_cost):
                    max_pro = (prices[i + 1] - low_cost)
        return max_pro
            
            