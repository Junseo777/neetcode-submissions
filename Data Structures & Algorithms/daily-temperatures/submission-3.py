class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i,t in enumerate(temperatures):
            for j,temp in enumerate(temperatures):
                if temp > t and j>i:
                    result.append(j-i)
                    break
                if j == (len(temperatures)-1):
                    result.append(0)
        return result
