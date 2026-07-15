import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven = 0
        for x in range(2, n * 2 + 1, 2):
            sumEven = sumEven + x
        sumOdd = 0
        for x in range(1, n * 2, 2):
            sumOdd = sumOdd + x
        return math.gcd(sumEven, sumOdd)
