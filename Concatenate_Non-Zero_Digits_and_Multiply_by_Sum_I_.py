class Solution:
    def sumAndMultiply(self, n: int) -> int:
        number = str(n)
        num = "".join([digit for digit in number if digit != "0"])
        if not num:
            return 0
        digits_sum = sum([int(digit) for digit in num])
        return int(num) * digits_sum
