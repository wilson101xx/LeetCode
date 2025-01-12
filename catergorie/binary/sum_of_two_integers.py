class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # if a < 0:
        #     sign = True
        #     a = abs(a)

        # index = 0
        # barray = [None] * a

        # for i, y in enumerate(barray):
        #     barray[i] = b

        # total = sum(barray)

        # print(total)
        barray = []
        barray.append(a)
        barray.append(b)
        total = sum(barray)
        print(total)

s = Solution()

s.getSum(2, 3)