class Solution(object):
    def numOfStrings(self, patterns, word):
        result = 0
        for char in patterns:
            if char in word:
                result += 1
        return result
