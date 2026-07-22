class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMap1 = {}
        for l in s:
            if l not in countMap1:
                countMap1[l]=1
            else:
                countMap1[l]+=1
        
        countMap2 = {}
        for l in t:
            if l not in countMap2:
                countMap2[l]=1
            else:
                countMap2[l]+=1

        if countMap1 == countMap2:
            return True
        else:
            return False
                
        