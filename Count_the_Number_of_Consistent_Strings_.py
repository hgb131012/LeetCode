class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        setted_allowed = set(allowed)
        count = 0
        for word in words:
            if all(c in allowed for c in word):
                count = count + 1
        return count
