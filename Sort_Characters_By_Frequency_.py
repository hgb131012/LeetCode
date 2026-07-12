class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        counts = Counter(s).most_common()
        for c in counts:
            result += c[0] * c[1]
        return result
