class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        uniques = [n for n in nums if counts[n] == 1]
        return sum(uniques)
