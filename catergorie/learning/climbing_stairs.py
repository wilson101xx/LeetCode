class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def rec(n):
            print(dp)
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            if n in dp:
                # print(dp)
                return dp[n]
            
            dp[n] = rec(n - 1) + rec(n-2)
            return dp[n]


        return rec(n)


s = Solution()
print(s.climbStairs(5))