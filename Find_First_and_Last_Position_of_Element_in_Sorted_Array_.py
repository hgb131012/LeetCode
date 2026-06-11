import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if bisect.bisect_left(nums, target) >= len(nums) or nums[bisect.bisect_left(nums, target)] != target:
            return [-1, -1]
        return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1]
