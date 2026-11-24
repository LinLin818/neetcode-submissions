class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Trying to find the minimum eating rate to eat all the bananas with a specific hour
        lo, hi = 1, max(piles)
        ans = hi
        while lo <= hi:
            k = (lo + hi) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                ans = k
                hi = k - 1
            else:
                lo = k + 1
        return ans
            