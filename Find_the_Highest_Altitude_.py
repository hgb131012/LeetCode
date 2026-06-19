class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum_altitudes = 0
        current_altitudes = 0
        for n in gain:
            current_altitudes += n
            maximum_altitudes = max(maximum_altitudes, current_altitudes)
        return maximum_altitudes
