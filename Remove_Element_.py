class Solution(object):
    def removeElement(self, nums, val):
        nums[:] = [n for n in nums if n != val]
