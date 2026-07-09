class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = []
        counts = Counter(arr)
        for n in arr:
            if counts[n] == n:
                result.append(n)
        if not result:
            return -1
        return max(result)
