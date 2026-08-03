class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = R
        while L<=R:
            mid = (R+L) // 2
            counter = 0
            
            for n in piles:
                
                try_one = n // mid
                if n % mid == 0:
                    counter += try_one
                else:
                    counter += try_one + 1
                
            if counter > h: 
                L = mid + 1
            elif counter <= h:
                res = min(res, mid)
                R = mid - 1
            
        
        return res
            