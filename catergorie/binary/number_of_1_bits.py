class Solution:
    def hammingWeight(self, n: int) -> int:
        
        b = bin(n)[2:].count("1")
        # x = b.count("1")
        # return x
        print(b)

        # count = 0
        # for i in b:
        #     if int(i) == 1:
        #         count+=1
        
        # return count

s = Solution()
print(s.hammingWeight(11))

    