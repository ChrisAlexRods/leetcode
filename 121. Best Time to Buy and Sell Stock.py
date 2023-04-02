class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize two pointers: left for the day we buy and right for the day we sell
        left, right = 0, 1

        # Initialize maxProfit variable to store the maximum profit we can achieve
        maxProfit = 0

        # Iterate through the prices list until the right pointer reaches the end
        while right < len(prices):

            # Check if the current buying day price is less than the current selling day price
            if prices[left] < prices[right]:

                # Calculate the profit from buying at left and selling at right
                profit = prices[right] - prices[left]

                # Update the maxProfit with the maximum value between the current maxProfit and profit
                maxProfit = max(maxProfit, profit)

            # If the current buying day price is greater than or equal to the selling day price
            else:

                # Move the left pointer to the right pointer's position to find a better buying day
                left = right

            # Move the right pointer to the next day
            right += 1

        # Return the maxProfit achieved
        return maxProfit


######################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1  #left day we buy, right day we sell
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit