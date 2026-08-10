class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        L = 0
        mp1= defaultdict(int)
        mp2={}
        for c in s1:
            if c not in mp2:
                mp2[c]=1
            else:
                mp2[c]+=1 
        
        
        for R in range(len(s2)):
            if R-L+1>k:
                if mp1[s2[L]] > 1:
                    mp1[s2[L]]-=1 
                else:
                    mp1.pop(s2[L])
                L+=1
                
            mp1[s2[R]]+=1

            if mp1 == mp2:
                return True

        return False
