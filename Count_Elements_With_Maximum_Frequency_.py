class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        result  = 0
        counts = Counter(nums)
        max_frequency = max(counts.values())
        for n in nums:
            if counts[n] == max_frequency:
                result = result + 1
        return result
