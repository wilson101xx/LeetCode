from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] * (amount + 1)
        dp[0] = 0


        for amount in range(1, len(dp)):
            for c in coins:
                if amount - c >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - c])

        return dp[amount] if dp[amount] != amount + 1 else -1
    
s = Solution()
print(s.coinChange([1,3,4,5], 7))

# s.testing([2,5,10,1], 11)