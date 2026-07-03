class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        result = []
        count = 0
        frequent = Counter(nums).most_common()
        for n in frequent:
            result.append(n[0])
            count += 1
            if count == k:
                return result
