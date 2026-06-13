class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate, missing = 0, 0
        counts = Counter(nums)
        for n in range(1, len(nums) + 1):
            if n not in counts:
                missing = n
            elif counts[n] > 1:
                duplicate = n
        return [duplicate, missing]
