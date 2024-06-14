class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0 
        for price in prices:
            if price < lowest: 
                lowest = price
            
            if ((price - lowest) > res):
                res = price - lowest
            
        return res

# T O(n), S O(n)
    
# NAIVE
# def maxProfit(self, prices: List[int]) -> int:
#     res = 0
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if (prices[j] - prices[i] > res):
#                 res = prices[j] - prices[i]

#     return res
# T O(n^2), S O(1)