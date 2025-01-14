#Using Fibunnaci sequence

class Solution:
    def climbStairs(self, n):
        if n <= 2:  # Base cases
            return n

        # Start with the first two steps
        first, second = 1, 2

        # Loop to calculate for higher steps
        for _ in range(3, n + 1):
            print(first, second)
            current = first + second  # Add the last two
            first, second = second, current  # Move up the staircase

        return second  # Return the final answer



s = Solution()
print(s.climbStairs(5))