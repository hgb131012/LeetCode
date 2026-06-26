class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        current_difference = nums[1] - nums[0]
        max_difference = nums[1] - nums[0]
        for i in range(1, len(nums)):
            current_difference = nums[i] - nums[i - 1]
            max_difference = max(max_difference, current_difference)
        return max_difference
