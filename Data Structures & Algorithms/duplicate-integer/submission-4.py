class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for n in nums:
            if n in countMap:
                return True
            else:
                countMap[n]=1
        return False