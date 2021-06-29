"""
Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

link --> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/s
"""

"""brute force approach"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            d1 = prices[i]
            for j in range(i, len(prices)):
                if profit < prices[j] - d1: 
                    profit = prices[j] -d1
        return profit


""" simple and awesome approach """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            if prices[i] - mn > profit:
                profit = prices[i] - mn
        return profit

# alternate but takes more time in execution.(fater than 23% whereas the above one was 85%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        profit = 0
        for i in range(len(prices)):
            mn = min(prices[i],mn)
            profit = max(profit, prices[i] - mn)
        return profit