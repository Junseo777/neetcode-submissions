class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        for i in range(len(nums)):
            L, R = 0, len(nums)-1
            while L < R:
                if L < R and L == i:
                    L+=1
                    continue
                if L <R and R == i:
                    R-=1
                    continue
                if nums[L] + nums[R] > -nums[i]:
                    R-=1
                elif nums[L]+nums[R] < -nums[i]:
                    L+=1
                elif nums[L]+nums[R] == -nums[i]:
                    sortedOut = [nums[i],nums[L],nums[R]]
                    sortedOut.sort()
                    sortedOutTuple = tuple(sortedOut)
                    output.add(sortedOutTuple)
                    L+=1
                    R-=1
      
        return(list(output))