from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        index = 0
        if edges[index][0] in edges[index+1]:
            num = edges[index][0]

        elif edges[index][1] in edges[index+1]:
            num = edges[index][1]

        return num
s = Solution()

s.findCenter([[1,2],[2,3],[4,2]])