class Solution:
    def reverseBits(self, n: int) -> int:

        array = []
        backwards=  bin(n)[2:][::-1]
        backwards = backwards.ljust(32, '0')
        print(backwards)

s = Solution()
print(s.reverseBits(0b00000010100101000001111010011100))