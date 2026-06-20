class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        times = len(nums) / 2
        for n in nums:
            if counts[n] > times:
                return n
