class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        nums1[:] = sorted(nums1 + nums2)
