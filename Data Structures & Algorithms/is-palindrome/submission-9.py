class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        L, R = 0, len(s)-1
        while L < R:

            while s[L].isalnum() == False and L<R:
                L+=1
            while s[R].isalnum() == False and L<R:
                R-=1
            
            s1 = s[L].lower()
            s2 = s[R].lower()

            if s1!=s2:
                return False
            L+=1
            R-=1
        return True
