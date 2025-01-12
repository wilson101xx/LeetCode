from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:        
        index = 0
        answer = []
        while index < n+1:
            answer.append(bin(index)[2:].count("1"))
            index+=1

        return answer

    def test(self, n):

        result = [0] * (n+1)

        for i in range(1, n+1):
            print(result[i >> 1] + (i & 1))

s = Solution()
print(s.countBits(5))
print(s.test(5))