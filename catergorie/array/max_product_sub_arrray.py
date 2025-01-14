# #Okay so i am going to start with the same as max_sub_array logic see how that goes
# # Okay worked however when only one negative interger in list getting a TypeError method object is not subscriptable going to try figure this



# from typing import List

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         print(nums)
#         len_of_array = len(nums)
#         if len_of_array < 2:
#             return nums[0]
        

#         current_num = 1
#         max_num = float('-inf')       

#         for i, num in enumerate(nums):
#             if (i+1) == len_of_array:
#                 current_num = max(num, current_num * num)
            
#             else:
#                 if 0 > current_num * num and nums[i+1] < 0:
#                     current_num = current_num * num
#                 else:
#                     current_num = max(num, current_num * num)

#             max_num = max(max_num, current_num)


#         print(max_num)



from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle the case of an empty array
        
        # Initialize variables to track the maximum and minimum products
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            
            result = max(result, max_product)
        
        return result

# Example usage
solution = Solution()
result = solution.maxProduct([2, 3, -2, 4])
print("Maximum Product:", result)

    
solution = Solution()


print(solution.maxProduct([2, -5,-2,-4,3]))
# print(solution.maxProduct([-2, 3, -4]))
