class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        times = len(nums) / 3
        result = []
        for n in nums:
            if counts[n] > times:
                result.append(n)
        return list(set(result))
