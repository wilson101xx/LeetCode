class Solution:


    def fib(self, n):

        dp = {}

        def rec(n):
            if n in dp:
                return dp[n]
            
            if n<=1:
                return n

            dp[n] = rec(n-1) + rec(n-2)
            return dp[n]
        print(rec(n))
        
s = Solution()

s.fib(500)