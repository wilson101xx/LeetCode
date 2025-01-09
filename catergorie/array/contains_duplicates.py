from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        length_of_array = len(nums)
        if length_of_array < 2:
            return False
        
        for postion, number in enumerate(nums):
            if postion+1 >= length_of_array:
                break
            print(f"number: {number}, num array + 1 {nums[postion+1]}")
            if number == nums[postion+1]:
                return True

        return False
    
    def better_version(self, nums: List[int]) -> bool:
        seen = set()

        for number in nums:
            if number in seen:
                return True
            seen.add(number)
            print(seen)
        return False
if __name__ == "__main__":
    solution = Solution()
    print(solution.better_version([2,14,18,22,22]))