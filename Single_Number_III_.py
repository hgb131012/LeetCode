class Solution(object):
    def singleNumber(self, nums):
        result = []
        counts = Counter(nums)
        for n in nums:
            if counts[n] == 1:
                result.append(n)
        return result
