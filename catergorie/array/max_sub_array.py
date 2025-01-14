from typing import List

#Thoughts
# have a current max
# thinking we can compare the current number against the sum of the previous sum plus current number to make sure we dont throw away individual intergers
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = 0
        max_num = float('-inf')       

        count = 0
        for num in nums:
            print(f"count = {count}     {num}   ,   {current_max}   +   {num}")
            current_max = max(num, current_max + num)
            print(f"count = {count}     {max_num}   ,   {current_max}")
            max_num = max(max_num, current_max)
            count +=1
        return max_num



solution = Solution()

print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

