from typing import List

class Solution:
    def twoSum(self, nums: List [int], target: int) -> List[int]:
        
        number_map = {}
        for position, number in enumerate(nums):
            missing_number = target - number
            if missing_number in number_map:
                return (number_map[missing_number], position)
            number_map[number] = position

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
