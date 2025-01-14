from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = [1] * len(nums)


        for i in range(len(nums) - 1, -1, -1):
            print
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+ LIS[j])
                    print(f"I = {i}     J = {j}")
        print(max(LIS))








s = Solution()
print(s.lengthOfLIS([1,2,4,3]))