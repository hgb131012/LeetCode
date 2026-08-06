class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for x in range(n, n + 11):
            digits = list(map(int, str(x)))
            digit_product = reduce(lambda a, b: a * b, digits) if len(digits) > 1 else x
            if digit_product % t == 0:
                return x
