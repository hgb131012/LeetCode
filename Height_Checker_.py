class Solution(object):
    def heightChecker(self, heights):
        result = 0
        expected = sorted(heights)
        for index, height in enumerate(heights):
            if height != expected[index]:
                result = result + 1
        return result
