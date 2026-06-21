class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()
        for c in costs:
            if coins >= c:
                count += 1
                coins -= c
            else:
                break
        return count
