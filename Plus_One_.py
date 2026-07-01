class Solution(object):
    def plusOne(self, digits):
        return list(map(int, str(1 + int("".join([str(n) for n in digits])))))
