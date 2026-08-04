class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def apply(a, b, op):
            if op == '+': return a + b
            elif op == '-': return a - b
            elif op == '*': return a * b
            elif op == '/': return int(a/b)

        def check(x):
            return (x in ('+', '-', '*', '/'))
        
        res = 0
        stack = []
        for i, num in enumerate(tokens):
            stack.append(num)
            if check(num):
                new_num = apply(int(stack[-3]),int(stack[-2]),stack[-1])
                for j in range(3):
                    stack.pop(-1)
                stack.append(new_num)
        
        res = int(stack[0])
        return res
        


