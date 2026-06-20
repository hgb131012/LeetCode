class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        result = []
        for n in nums:
            if(counts[n] == 1) and (n-1 not in counts and n+1 not in counts):
                result.append(n)
        return result
