class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       current_sum = nums[0]
       maximum_sum = nums[0]
       for num in nums[1:]:
          current_sum = max(num, current_sum + num)
          maximum_sum = max(current_sum, maximum_sum)
       return maximum_sum
