class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for x in nums:
            count = 0
            for y in nums:
                if y != x and y < x:
                    count += 1
            result.append(count)
        return result
