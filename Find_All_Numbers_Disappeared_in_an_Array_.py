import bisect
class Solution(object):
    def findDisappearedNumbers(self, nums):
        result = []
        numbers = set(nums)
        for n in range(1, len(nums) + 1):
            if n not in numbers:
                bisect.insort(result, n)
        return result
