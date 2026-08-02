class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R = 0, len(numbers)-1
        res = []
        while L < R:
            if numbers[L]+numbers[R]>target:
                R-=1
            elif numbers[L]+numbers[R]<target:
                L+=1
            else:
                break
        res.append(L+1)
        res.append(R+1)
        return res