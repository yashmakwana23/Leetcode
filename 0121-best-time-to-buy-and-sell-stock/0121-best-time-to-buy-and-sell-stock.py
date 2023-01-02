class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ans = 0
        for r in range(1 ,len(prices)):
            ans = max(ans, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
        return ans