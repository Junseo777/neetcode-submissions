class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        res = 0
        mp = {}
        maxf = 0

        for R in range(len(s)):

            
            if s[R] not in mp:
                mp[s[R]]=1
            else:
                mp[s[R]]+=1
            
            maxf = max(maxf, mp[s[R]])

            if R-L+1 -maxf > k:
                mp[s[L]]-=1
                L+=1
            
            res = max(res,R-L+1)

        return res

            