class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        st, nd = 0, 0
        result = []
        while st < len(nums1) and nd < len(nums2):
            if nums1[st] == nums2[nd]:
                result.append(nums1[st])
                st = st + 1
                nd = nd + 1
            elif nums1[st] < nums2[nd]:
                st = st + 1
            else:
                nd = nd + 1
        return result
