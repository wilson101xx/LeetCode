from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        copy_nums = nums.copy()
        
        cur = 0 
        working = True
        while working == True:
            if len(answer) == len(copy_nums):
                working == False
                break
            copy_nums.pop(cur)
            current = 1
            
            for i in copy_nums:
                current = current * i
            answer.append(current)
            copy_nums = nums.copy()
            cur += 1
        return answer

    def betterProductExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        print(output)

        prefix = 1
        for i in range(n):
            print("i: ",i)
            print("nums: ", nums[i])
            print("prefix: ", prefix)
            output[i] = prefix
            prefix *= nums[i]
        print(output)

if __name__ == "__main__":
    solution = Solution()
    print(solution.betterProductExceptSelf([1,2,3,4]))
    # print(solution.betterProductExceptSelf([-1,1,0,-3,3]))