from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        for i in range(length+1):
            if i == length:
                return i
            elif i != nums[i]:
                return i
            

s = Solution()


print(s.missingNumber([0,1]))
# print(s.missingNumber([9,6,4,2,3,5,7,0,1]))