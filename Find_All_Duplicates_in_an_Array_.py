import bisect
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        counts = Counter(nums)
        for n in nums:
            if counts[n] > 1:
                bisect.insort(result, n)
        return list(set(result))
