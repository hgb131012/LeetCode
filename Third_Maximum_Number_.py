class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        first_max = max(nums)
        second_max = max([n for n in nums if n != first_max])
        return max([n for n in nums if n != first_max and n != second_max])
