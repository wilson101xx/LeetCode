
# SO this works, but next we need to see if we can make it faster as at 5% so can we do it with recessive programming
# and dp caching


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        biggest_sub_array = []
        current_sub_array = []
        max_sub = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            sub_index = i
            print("I: ", i)
            while sub_index < len(s):
                print(f"Position {sub_index},   Letter = {s[sub_index]}     array = {current_sub_array}")
                if s[sub_index] in current_sub_array:
                    print(f" Bigget_sub_array {biggest_sub_array},  current sub array {current_sub_array}")
                    if len(biggest_sub_array) < len(current_sub_array):
                        biggest_sub_array = current_sub_array
                    current_sub_array = []
                    max_sub = len(biggest_sub_array)
                    break
                else:
                    current_sub_array.append(s[sub_index])

                sub_index += 1
            

        print(biggest_sub_array)
        return max_sub

s = Solution()
# s.lengthOfLongestSubstring("abcabcbb")
print(s.lengthOfLongestSubstring("jbpnbwwd"))