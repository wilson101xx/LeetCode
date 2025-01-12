"""
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


i would need a current largest number.
I would need a for loop to iterate over the array, if the current number is larger than the current Max number than replace

currnet = nums[0]

for i in nums[]:
    if i > current max:
    
    current max = 2 x 3
    if 2 x 3 x -2 > current max:

        replace current max with value

    else:
        current max stays the same

    what is 3 x -2:
        if 3 x -2 > current max:
            replace
        
        else
    what is -2 x 4


"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max = 0
        min = 0
        index = 0
        length_of_list = len(list)
        
        while index < length_of_list:

            




s = Solution()
# s.maxProduct([])
s.maxProduct([0,2,4]) # 8
s.maxProduct([2,3,-2,4]) # 6
s.maxProduct([-3,0,1,-2]) # 1
# s.maxProduct([-2,-3,7, -2]) #42
# s.maxProduct([0,2]) # 2
# s.maxProduct([2,3,-2,4]) #Expected 6
s.maxProduct([-2,3,-4]) # 24