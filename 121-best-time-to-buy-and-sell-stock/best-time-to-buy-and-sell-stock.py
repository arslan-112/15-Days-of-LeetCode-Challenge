class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        max = 0
        curr_prof = 0
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            curr_prof = prices[i] - lowest
            if curr_prof > max:
                max = curr_prof
        
        return max
    