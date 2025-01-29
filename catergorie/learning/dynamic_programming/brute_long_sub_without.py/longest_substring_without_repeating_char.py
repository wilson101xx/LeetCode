class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = {}
        seen = set()


        def rec(start, seen):
            #Making sure index is in range
            if start >= len(s):
                return 0
            
            if start in dp:
                return dp[start]

            if s[start] in seen:
                return 0 
            
            seen.add(s[start])
            print(seen)
            max_length = rec(start+1, seen)
            return max_length


        for start in range(len(s)):
            print(rec(start, set()))

        print(seen)
s = Solution()

s.lengthOfLongestSubstring("abcabcbb")