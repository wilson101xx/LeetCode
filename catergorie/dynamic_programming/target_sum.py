from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(index, total, path):
            print(dp)
            if index == len(nums):
                if total == target:
                    print(f"Valid Path: {path}, Total: {total}")
                    return 1
                else:
                    return 0
            if (index, total) in dp:
                return dp[(index, total)]

            add_path = path + [f"+{nums[index]}"]
            subtract_path = path + [f"-{nums[index]}"]

            dp[(index, total)] = (
                backtrack(index + 1, total + nums[index], add_path) +
                backtrack(index + 1, total - nums[index], subtract_path)
            )
            return dp[(index, total)]

        return backtrack(0, 0, [])

s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
