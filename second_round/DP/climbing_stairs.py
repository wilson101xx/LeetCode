class Solution:
    def climbStairs(self, n: int) -> int:
        # Dictionary to store already computed results
        memo = {}

        def helper(steps):
            if steps <= 2:  # Base cases
                return steps
            
            # Check if already computed
            if steps in memo:
                return memo[steps]
            
            # Recursive calculation with memoization
            memo[steps] = helper(steps - 1) + helper(steps - 2)
            return memo[steps]
        
        return helper(n)


s = Solution()
print(s.climbStairs(5))