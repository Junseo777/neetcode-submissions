class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R = 0, len(heights)-1
        area = (R-L) * min(heights[L],heights[R])
        while L < R:
            if heights[L]<heights[R]:
                L+=1
            elif heights[L]>heights[R]:
                R-=1
            else:
                L+=1
                R-=1

            area = max(area, (R-L) * min(heights[L],heights[R]))
        return area