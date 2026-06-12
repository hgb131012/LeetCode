class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = [n for n in nums if n == 0]
        non_zero = [n for n in nums if n != 0]
        nums[:] = non_zero + zeros
