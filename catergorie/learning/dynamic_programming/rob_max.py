from typing import List

class learning:
    def rob_max(self, houses: List[int]) -> int:
        length = len(houses)
        # print(length)
        rob = max(houses[0] + rob[2:length])

l = learning()
l.rob_max([1,2,3,1])