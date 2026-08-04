 class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        numbers = set(nums)
        counts = Counter(list(range(min(nums), max(nums))))
        return [n for n in counts if n not in numbers]
