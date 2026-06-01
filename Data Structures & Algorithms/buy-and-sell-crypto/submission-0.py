class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left = buy, right = sell
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
'''
    Here we check if the buy rate is lowest by checking the diff between l n r
    we store this diff in a var, and compare this diff at each iter and return the max
'''