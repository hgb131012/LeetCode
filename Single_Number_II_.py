class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for n in counts:
            if counts[n] == 1:
                return n
