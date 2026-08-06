class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [] 
        
        def prefixProduct():
            prefix = []
            total = 1
            for n in nums:
                total=total*n
                prefix.append(total)
            return prefix

        def postfixProduct():
            postfix = []
            total = 1
            for n in reversed(nums):
                total = total*n
                postfix.append(total)
            return postfix
        
        x=prefixProduct()
        y=postfixProduct()

        for i,n in enumerate(nums):

            b = x[i-1] if (i-1) >= 0 else 1
            
            a = y[-2-i] if (2+i) <= len(nums) else 1

            output.append(a * b)

        return output





