class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(nums)
        for n in range(0, len(nums) + 1):
            if n not in numbers:
                return n
